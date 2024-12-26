def calculate_average(numbers):
    """
    Menghitung rata-rata dari daftar angka.
    
    Parameters:
        numbers (list): Daftar angka.
    
    Returns:
        float: Nilai rata-rata.
    """
    if not numbers:
        raise ValueError("Daftar angka tidak boleh kosong.")
    
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Hitung rata-rata dari daftar angka.")
    parser.add_argument(
        "numbers",
        metavar="N",
        type=float,
        nargs="+",
        help="Angka-angka yang ingin dihitung rata-ratanya.",
    )
    args = parser.parse_args()
    
    try:
        result = calculate_average(args.numbers)
        print(f"Rata-rata: {result}")
    except ValueError as e:
        print(f"Error: {e}")
