def main():
    message_file = 'files.txt'
    print(decode(message_file))


def decode(message_file):
    pyramid = {}

    with open(message_file, 'r') as file:
        for line in file:

            num , word = line.split()
            pyramid[num] = word
       

    max_num = max(pyramid.keys())
    index = 0
    row =''
    for i in range(1,int(max_num)):
        index += i
      
        if str(index) in pyramid: 
          row += ''.join(pyramid[str(index)]) + ' '
        

    decoded_message = row
    return decoded_message.lower().strip()

main()