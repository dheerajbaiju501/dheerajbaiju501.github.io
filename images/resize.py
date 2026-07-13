from PIL import Image

def resize_to_match(source_path, target_path, output_path):
    # Open both images
    src = Image.open(source_path)
    tgt = Image.open(target_path)

    # Get target image size
    target_size = tgt.size  # (width, height)

    # Resize source image
    resized = src.resize(target_size, Image.LANCZOS)

    # Save output
    resized.save(output_path)
    print(f"Saved resized image to {output_path} with size {target_size}")

# Example usage
resize_to_match("WhatsApp Image 2025-10-30 at 19.19.01.jpg", "portrait.jpg", "resized.jpg")
