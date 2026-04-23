def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort() # 1 ordernar la lista, para indentificar mejor duplicados
    result = []

    for i in range(len(nums )- 2): # se le resta - 2 porque hay que guardar espacio para los 2 números restantes
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1 # definimos los punteros para encontrar los 2 números siguientes del triplete
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                # empezar a saltar los duplicados
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right  and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1
    return result



if __name__ == "__main__":
    print(threeSum([-1, 0, 1, 2, -1, -4])) # Output: [[-1, -1, 2], [-1, 0, 1]]
