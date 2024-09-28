class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1

        current_char = chars[0]
        current_count = 1
        last_char_index = 0

        for i in range(1, len(chars) + 1):
            if i == len(chars):
                if current_count > 1:
                    chars[last_char_index + 1] = str(current_count)
                break

            char = chars[i]
            if char == current_char:
                current_count += 1
                chars[i] = None

            elif current_count > 1:
                chars[last_char_index + 1] = str(current_count)
                current_count = 1
                current_char = chars[i]
                last_char_index = i
            else:
                current_count = 1
                current_char = chars[i]
                last_char_index = i

        for i in range(len(chars)):
            if not chars[i] or not chars[i].isnumeric():
                continue

            num = chars[i]
            if len(num) == 1:
                continue

            j = i + len(num) - 1
            num = int(num)
            while j >= i:
                chars[j] = str(num % 10)
                num = num // 10
                j -= 1

        write_index = 0

        for char in chars:
            if char != None:
                chars[write_index] = char
                write_index += 1

        return write_index
