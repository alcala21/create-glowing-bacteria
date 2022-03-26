from hstest import StageTest, dynamic_test, TestedProgram, WrongAnswer, CheckResult

correct_parts = ["GACGTCTGTGCAAGTACTACTGTTC", "TGCAGTCACTTGAATTCGATACCCAGCTGTTATTTGTATAGTTCA",
                 "CTGCAGACACGTTCATGATGACAAGACGT", "CAGTGAACTTAAGCTATGGGTCGACAATAAACATATCAAGT"]


class RestrictionMakingTest(StageTest):

    @dynamic_test()
    def test(self):
        program = TestedProgram()
        program.start()

        if not program.is_waiting_input():
            raise WrongAnswer("You program should input the string")

        reply = program.execute(
            """GACGTCTGTGCAAGTACTACTGTTCTGCAGTCACTTGAATTCGATACCCAGCTGTTATTTGTATAGTTCA CTGCAGACACGTTCATGATGACAAGACGTCAGTGAACTTAAGCTATGGGTCGACAATAAACATATCAAGT""")
        if not reply.strip():
            raise WrongAnswer("Your answer is an empty string")

        # change reply to list format
        reply_list = reply.strip().split()

        if len(reply_list) != 4:
            raise WrongAnswer("Your answer should have four fragments. Two fragments on each line")

        parts_len = [len(reply_list[0]), len(reply_list[1]), len(reply_list[2]), len(reply_list[3])]

        if parts_len != [25, 45, 29, 41]:
            raise WrongAnswer("One of four fragments has a wrong length.\n"
                              "Check if each of the protruding ends is 4 nucleotides in length.")
        else:
            for part in reply_list:
                if part not in correct_parts:
                    raise WrongAnswer(f"This part \"{part}\" of the final output is wrong.\n"
                                      f"Pay attention on the restriction site and plasmid sequence.")
            else:
                return CheckResult.correct()


if __name__ == '__main__':
    RestrictionMakingTest().run_tests()
