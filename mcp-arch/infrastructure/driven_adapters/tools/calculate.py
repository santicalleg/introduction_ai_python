class Calculate():

    async def add(self, num1: int, num2: int) -> int:
        """
        Add a number to the current value.

        Args:
            num1 (int): The first number to add.
            num2 (int): The second number to add.
        Returns:
            int: The sum of the current value and the two numbers.
        
        """
        return num1 + num2

    async def subtract(self, num1: int, num2: int) -> int:
        """
        Subtract a number from the current value.
        Args:
            num1 (int): The first number to subtract.
            num2 (int): The second number to subtract.
        Returns:
            int: The difference of the current value and the two numbers.
        """
        if (num1 < 0 or num2 < 0):
            raise ValueError("Both numbers must be non-negative integers.")
        if (num1 < num2):
            raise ValueError("The first number must be greater than or equal to the second number.")

        return num1 - num2