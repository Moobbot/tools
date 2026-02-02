"""Simple image upscaler with optional OpenCV DNN Super Resolution."""

import argparse
from pathlib import Path
import cv2


INTERP_MAP = {
    "nearest": cv2.INTER_NEAREST,
    "linear": cv2.INTER_LINEAR,
    "cubic": cv2.INTER_CUBIC,
    "lanczos": cv2.INTER_LANCZOS4,
}


# Defaults so you can just run `python upsize_img.py` directly
DEFAULT_INPUT = "images/1_4.jpg"
DEFAULT_OUTPUT = "upscaled/1_4.jpg"
DEFAULT_SCALE = 4.0


def upscale_with_superres(img, scale: int, model_path: Path, model_name: str):
    """Try to upscale using OpenCV DNN Super Resolution if available."""

    try:
        from cv2 import dnn_superres  # type: ignore
    except ImportError:
        return None, "OpenCV build lacks dnn_superres"

    if not model_path.exists():
        return None, f"Model not found: {model_path}"

    sr = dnn_superres.DnnSuperResImpl_create()
    sr.readModel(str(model_path))
    sr.setModel(model_name.lower(), scale)
    return sr.upsample(img), None


def parse_args():
    parser = argparse.ArgumentParser(description="Upscale an image")
    parser.add_argument(
        "input",
        nargs="?",
        default=DEFAULT_INPUT,
        help="Input image path (default: %(default)s)",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=DEFAULT_OUTPUT,
        help="Output image path",
    )
    parser.add_argument(
        "-s",
        "--scale",
        type=float,
        default=DEFAULT_SCALE,
        help="Upscale factor",
    )
    parser.add_argument(
        "-i",
        "--interp",
        choices=INTERP_MAP.keys(),
        default="cubic",
        help="Interpolation when not using DNN SR",
    )
    parser.add_argument(
        "-m",
        "--model",
        type=Path,
        help="Path to DNN super-resolution model (e.g. ESPCN_x2.pb)",
    )
    parser.add_argument(
        "--model-name",
        choices=["espcn", "edsr", "fsrcnn", "lapsrn"],
        default="espcn",
        help="Model family used with --model",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    img = cv2.imread(args.input)
    if img is None:
        raise SystemExit(f"Could not read input image: {args.input}")

    upscaled = None
    if args.model:
        upscaled, err = upscale_with_superres(
            img, int(args.scale), args.model, args.model_name
        )
        if err:
            print(f"[warn] {err}. Falling back to interpolation.")

    if upscaled is None:
        interp = INTERP_MAP[args.interp]
        upscaled = cv2.resize(
            img, None, fx=args.scale, fy=args.scale, interpolation=interp
        )

    cv2.imwrite(args.output, upscaled)
    print(f"Saved: {args.output}")


if __name__ == "__main__":
    main()
