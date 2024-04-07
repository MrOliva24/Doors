from Door import *
from CodeHandler import *



if __name__ == "__main__":


    open_code = "1234"
    fire_code = "5678"
    unlock_code = "0000"
    chain1 = Log(Unlock(unlock_code, FireAlarm(fire_code, Open(open_code, Lock(None)))))
    chain2 = Log(Open(open_code, None))
    chain3 = Log(FireAlarm(fire_code, Open(open_code, None)))
    d1 = Door('d1', chain1)

    def process(d1):
        d1.reset_state()
        d1.process_code('1234')  # opens
        d1.process_code('5678')  # opens and fires alarm
        d1.process_code('1111')  # first trial
        d1.process_code('4321')  # second trial
        d1.process_code('5555')  # thrid trial, gets locked
        d1.process_code('6666')  # invalid unlock code
        d1.process_code('7777')  # invalid unlock code
        d1.process_code('1111')  # invalid unlock code
        d1.process_code('0000')  # valid unlock code, now can be opened or fire alarm

    process(d1)
    d1.reset_state()
    d1._code_handler = chain2
    print("\n------------------------------------\n")
    process(d1)
    d1.reset_state()
    d1._code_handler = chain3
    print("\n------------------------------------\n")
    process(d1)


