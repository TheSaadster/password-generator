# Password Generator

This is a Python script that generates random passwords based on user-defined criteria such as minimum length, inclusion of numbers, and inclusion of special characters.

## Usage

1. Run the script.
```
python main.py
```
2. Enter the minimum length of the password when prompted.
3. Choose whether you want numbers in your password by entering 'y' for yes or 'n' for no.
4. Choose whether you want special characters in your password by entering 'y' for yes or 'n' for no.
5. The generated password will be displayed.

## Functionality

- The script utilizes the `random` and `string` modules in Python to generate random passwords.
- It allows customization of password length, inclusion of numbers, and inclusion of special characters.
- The script ensures that the generated password meets the specified criteria.

## Parameters

- `min_length`: Minimum length of the password.
- `numbers`: Boolean indicating whether numbers should be included in the password.
- `special_characters`: Boolean indicating whether special characters should be included in the password.

## Sample Output

```
Enter the minimum length of the password: 8
Do you want numbers in your password? (y/n): y
Do you want special characters in your password? (y/n): y
The generated password is: A#7n2$Fp

```
