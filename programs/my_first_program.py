class Party:
    def __init__(self, name):
        self.name = name

class Input:
    def __init__(self, name, party):
        self.name = name
        self.party = party

class SecretInteger:
    def __init__(self, input_obj, value):
        self.input_obj = input_obj
        self.value = value

class Output:
    def __init__(self, secret_int, name, party):
        self.name = name
        self.party = party
        self.value = secret_int.value

def main():
    party1 = Party(name="Party1")
    
    # Assign values to my_int1 and my_int2 (in a real-world scenario, these values would come from the respective party's input)
    my_int1 = SecretInteger(Input(name="my_int1", party=party1), value=42)
    my_int2 = SecretInteger(Input(name="my_int2", party=party1), value=58)

    # New computation: Add my_int1 and my_int2
    result_value = my_int1.value + my_int2.value

    output = Output(SecretInteger(Input(name="result", party=party1), value=result_value), "result_output", party1)
    return [output]

if __name__ == "__main__":
    result = main()
    for output in result:
        print(f"Output Name: {output.name}, Party: {output.party.name}, Value: {output.value}")
