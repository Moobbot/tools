import fitz  # pymupdf
import argparse
import os
import sys


def convert_pdf_to_png(pdf_path, output_folder, dpi=300):
    """
    Converts a PDF file to high-quality PNG images.

    Args:
        pdf_path (str): Path to the source PDF file.
        output_folder (str): Path to the destination folder.
        dpi (int): Dots per inch for the output images. Higher means better quality.
    """
    if not os.path.exists(pdf_path):
        print(f"Error: PDF file not found at {pdf_path}")
        return

    # Create output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created output directory: {output_folder}")

    try:
        doc = fitz.open(pdf_path)
        print(f"Opened PDF: {pdf_path}")
        print(f"Total pages: {len(doc)}")

        for page_num in range(len(doc)):
            page = doc.load_page(page_num)

            # Zoom logic: 72 dpi is the default scale (1.0).
            # To get higher DPI, we increase the zoom matrix.
            zoom = dpi / 72
            mat = fitz.Matrix(zoom, zoom)

            pix = page.get_pixmap(matrix=mat)

            output_filename = os.path.join(
                output_folder, f"page_{page_num + 1:03d}.png"
            )
            pix.save(output_filename)

            print(f"Saved: {output_filename}")

        print("Conversion complete!")
        doc.close()

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Convert PDF pages to high-quality PNG images."
    )
    parser.add_argument(
        "pdf_path",
        nargs="?",
        help="Path to the input PDF file",
        default="datasets/AIRC_2025_Position_Global_Reach.pdf",
    )
    parser.add_argument(
        "--output",
        "-o",
        default="output_images/AIRC_2025_Position_Global_Reach",
        help="Output directory for PNGs (default: output_images)",
    )
    parser.add_argument(
        "--dpi",
        "-d",
        type=int,
        default=300,
        help="DPI for the output images (default: 300)",
    )

    args = parser.parse_args()

    convert_pdf_to_png(args.pdf_path, args.output, args.dpi)


if __name__ == "__main__":
    main()
