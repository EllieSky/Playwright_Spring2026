def generate_formatted_id():
    # 1. Ask for user information
    full_name = input("Enter your full name: ").strip()
    year_input = input("Enter your birth year (e.g., 1995): ").strip()
    favorite_color = input("Enter your favorite color: ")
    favorite_color = favorite_color.strip() # can also do it on a separate line
    # favorite_color = favorite_color.upper() # convert all letters to upper case either here or at the end


    # 2. Validate: Is the name at least 2 words?
    # Using count(' ') to ensure there is at least one space
    if full_name.count(' ') < 1:
        print("Error: Name must contain at least two words.")
        return None

    # 3. Validate: Is birth year reasonable?
    # First, check if the input is numeric
    if not year_input.isdigit():
        print("Error: Birth year must be a valid number.")
        return None

    birth_year = int(year_input)
    if birth_year <= 1900:
        print("Error: Birth year must be after 1900.")
        return None

    # 4. Generate initials using slicing and list comprehension
    # Splits name into words and takes the 0th index of each
    first, last = "", ""
    name_parts = full_name.split()
    if len(name_parts) == 3:
        first, _, last = name_parts

    if len(name_parts) == 2:
        first, last = name_parts

    initials = first[0].upper() + last[0].upper()

    # 5. Calculate age (using 2026 as the current year)
    current_year = 2026
    age = current_year - birth_year

    # 6. Create the formatted code: INITIALS-AGE-COLOR
    formatted_id = f"{initials}-{age}-{favorite_color.upper()}"

    return formatted_id


# Example usage:
result = generate_formatted_id()
if result:
    print(f"ID Created: {result}")