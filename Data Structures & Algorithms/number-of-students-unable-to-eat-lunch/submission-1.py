class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        consec_fail=0

        while consec_fail<len(students):
            if students[0]==sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                consec_fail=0
            else:
                students.append(students.pop(0))
                consec_fail += 1

        return len(students)
        