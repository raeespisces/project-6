class Bank:
    bank_name = "UBL"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name


if __name__=="__main__":
        
        user1 = Bank()
        user2 = Bank()

        print ("Old bank name")
        print(f"user1 bank name : {user1.bank_name}")
        print(f"user2 bank nmame : {user2.bank_name}")
        
        Bank.change_bank_name("Mezan Bank")

        print("\nNew Bank Name")

        print(f"\nuser1 bank name : {user1.bank_name}")
        print(f"user2 bank name : {user2.bank_name}")

