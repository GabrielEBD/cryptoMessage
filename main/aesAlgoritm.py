
isbox = [82, 9, 106, 213, 48, 54, 165, 56, 191, 64, 163, 158, 129, 243, 215, 251, 124, 227, 57, 130, 155, 47, 255, 135, 52, 142, 67, 68, 196, 222, 233, 203, 84, 123, 148, 50, 166, 194, 35, 61, 238, 76, 149, 11, 66, 250, 195, 78, 8, 46, 161, 102, 40, 217, 36, 178, 118, 91, 162, 73, 109, 139, 209, 37, 114, 248, 246, 100, 134, 104, 152, 22, 212, 164, 92, 204, 93, 101, 182, 146, 108, 112, 72, 80, 253, 237, 185, 218, 94, 21, 70, 87, 167, 141, 157, 132, 144, 216, 171, 0, 140, 188, 211, 10, 247, 228, 88, 5, 184, 179, 69, 6, 208, 44, 30, 143, 202, 63, 15, 2, 193, 175, 189, 3, 1, 19, 138, 107, 58, 145, 17, 65, 79, 103, 220, 234, 151, 242, 207, 206, 240, 180, 230, 115, 150, 172, 116, 34, 231, 173, 53, 133, 226, 249, 55, 232, 28, 117, 223, 110, 71, 241, 26, 113, 29, 41, 197, 137, 111, 183, 98, 14, 170, 24, 190, 27, 252, 86, 62, 75, 198, 210, 121, 32, 154, 219, 192, 254, 120, 205, 90, 244, 31, 221, 168, 51, 136, 7, 199, 49, 177, 18, 16, 89, 39, 128, 236, 95, 96, 81, 127, 169, 25, 181, 74, 13, 45, 229, 122, 159, 147, 201, 156, 239, 160, 224, 59, 77, 174, 42, 245, 176, 200, 235, 187, 60, 131, 83, 153, 97, 23, 43, 4, 126, 186, 119, 214, 38, 225, 105, 20, 99, 85, 33, 12, 125]

sbox = [99, 124, 119, 123, 242, 107, 111, 197, 48, 1, 103, 43, 254, 215, 171, 118, 202, 130, 201, 125, 250, 89, 71, 240, 173, 212, 162, 175, 156, 164, 114, 192, 183, 253, 147, 38, 54, 63, 247, 204, 52, 165, 229, 241, 113, 216, 49, 21, 4, 199, 35, 195, 24, 150, 5, 154, 7, 18, 128, 226, 235, 39, 178, 117, 9, 131, 44, 26, 27, 110, 90, 160, 82, 59, 214, 179, 41, 227, 47, 132, 83, 209, 0, 237, 32, 252, 177, 91, 106, 203, 190, 57, 74, 76, 88, 207, 208, 239, 170, 251, 67, 77, 51, 133, 69, 249, 2, 127, 80, 60, 159, 168, 81, 163, 64, 143, 146, 157, 56, 245, 188, 182, 218, 33, 16, 255, 243, 210, 205, 12, 19, 236, 95, 151, 68, 23, 196, 167, 126, 61, 100, 93, 25, 115, 96, 129, 79, 220, 34, 42, 144, 136, 70, 238, 184, 20, 222, 94, 11, 219, 224, 50, 58, 10, 73, 6, 36, 92, 194, 211, 172, 98, 145, 149, 228, 121, 231, 200, 55, 109, 141, 213, 78, 169, 108, 86, 244, 234, 101, 122, 174, 8, 186, 120, 37, 46, 28, 166, 180, 198, 232, 221, 116, 31, 75, 189, 139, 138, 112, 62, 181, 102, 72, 3, 246, 14, 97, 53, 87, 185, 134, 193, 29, 158, 225, 248, 152, 17, 105, 217, 142, 148, 155, 30, 135, 233, 206, 85, 40, 223, 140, 161, 137, 13, 191, 230, 66, 104, 65, 153, 45, 15, 176, 84, 187, 22]

gfp2 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200, 202, 204, 206, 208, 210, 212, 214, 216, 218, 220, 222, 224, 226, 228, 230, 232, 234, 236, 238, 240, 242, 244, 246, 248, 250, 252, 254, 27, 25, 31, 29, 19, 17, 23, 21, 11, 9, 15, 13, 3, 1, 7, 5, 59, 57, 63, 61, 51, 49, 55, 53, 43, 41, 47, 45, 35, 33, 39, 37, 91, 89, 95, 93, 83, 81, 87, 85, 75, 73, 79, 77, 67, 65, 71, 69, 123, 121, 127, 125, 115, 113, 119, 117, 107, 105, 111, 109, 99, 97, 103, 101, 155, 153, 159, 157, 147, 145, 151, 149, 139, 137, 143, 141, 131, 129, 135, 133, 187, 185, 191, 189, 179, 177, 183, 181, 171, 169, 175, 173, 163, 161, 167, 165, 219, 217, 223, 221, 211, 209, 215, 213, 203, 201, 207, 205, 195, 193, 199, 197, 251, 249, 255, 253, 243, 241, 247, 245, 235, 233, 239, 237, 227, 225, 231, 229]

gfp3 = [0, 3, 6, 5, 12, 15, 10, 9, 24, 27, 30, 29, 20, 23, 18, 17, 48, 51, 54, 53, 60, 63, 58, 57, 40, 43, 46, 45, 36, 39, 34, 33, 96, 99, 102, 101, 108, 111, 106, 105, 120, 123, 126, 125, 116, 119, 114, 113, 80, 83, 86, 85, 92, 95, 90, 89, 72, 75, 78, 77, 68, 71, 66, 65, 192, 195, 198, 197, 204, 207, 202, 201, 216, 219, 222, 221, 212, 215, 210, 209, 240, 243, 246, 245, 252, 255, 250, 249, 232, 235, 238, 237, 228, 231, 226, 225, 160, 163, 166, 165, 172, 175, 170, 169, 184, 187, 190, 189, 180, 183, 178, 177, 144, 147, 150, 149, 156, 159, 154, 153, 136, 139, 142, 141, 132, 135, 130, 129, 155, 152, 157, 158, 151, 148, 145, 146, 131, 128, 133, 134, 143, 140, 137, 138, 171, 168, 173, 174, 167, 164, 161, 162, 179, 176, 181, 182, 191, 188, 185, 186, 251, 248, 253, 254, 247, 244, 241, 242, 227, 224, 229, 230, 239, 236, 233, 234, 203, 200, 205, 206, 199, 196, 193, 194, 211, 208, 213, 214, 223, 220, 217, 218, 91, 88, 93, 94, 87, 84, 81, 82, 67, 64, 69, 70, 79, 76, 73, 74, 107, 104, 109, 110, 103, 100, 97, 98, 115, 112, 117, 118, 127, 124, 121, 122, 59, 56, 61, 62, 55, 52, 49, 50, 35, 32, 37, 38, 47, 44, 41, 42, 11, 8, 13, 14, 7, 4, 1, 2, 19, 16, 21, 22, 31, 28, 25, 26]

gfp9 = [0, 9, 18, 27, 36, 45, 54, 63, 72, 65, 90, 83, 108, 101, 126, 119, 144, 153, 130, 139, 180, 189, 166, 175, 216, 209, 202, 195, 252, 245, 238, 231, 59, 50, 41, 32, 31, 22, 13, 4, 115, 122, 97, 104, 87, 94, 69, 76, 171, 162, 185, 176, 143, 134, 157, 148, 227, 234, 241, 248, 199, 206, 213, 220, 118, 127, 100, 109, 82, 91, 64, 73, 62, 55, 44, 37, 26, 19, 8, 1, 230, 239, 244, 253, 194, 203, 208, 217, 174, 167, 188, 181, 138, 131, 152, 145, 77, 68, 95, 86, 105, 96, 123, 114, 5, 12, 23, 30, 33, 40, 51, 58, 221, 212, 207, 198, 249, 240, 235, 226, 149, 156, 135, 142, 177, 184, 163, 170, 236, 229, 254, 247, 200, 193, 218, 211, 164, 173, 182, 191, 128, 137, 146, 155, 124, 117, 110, 103, 88, 81, 74, 67, 52, 61, 38, 47, 16, 25, 2, 11, 215, 222, 197, 204, 243, 250, 225, 232, 159, 150, 141, 132, 187, 178, 169, 160, 71, 78, 85, 92, 99, 106, 113, 120, 15, 6, 29, 20, 43, 34, 57, 48, 154, 147, 136, 129, 190, 183, 172, 165, 210, 219, 192, 201, 246, 255, 228, 237, 10, 3, 24, 17, 46, 39, 60, 53, 66, 75, 80, 89, 102, 111, 116, 125, 161, 168, 179, 186, 133, 140, 151, 158, 233, 224, 251, 242, 205, 196, 223, 214, 49, 56, 35, 42, 21, 28, 7, 14, 121, 112, 107, 98, 93, 84, 79, 70]

gfp11 = [0, 11, 22, 29, 44, 39, 58, 49, 88, 83, 78, 69, 116, 127, 98, 105, 176, 187, 166, 173, 156, 151, 138, 129, 232, 227, 254, 245, 196, 207, 210, 217, 123, 112, 109, 102, 87, 92, 65, 74, 35, 40, 53, 62, 15, 4, 25, 18, 203, 192, 221, 214, 231, 236, 241, 250, 147, 152, 133, 142, 191, 180, 169, 162, 246, 253, 224, 235, 218, 209, 204, 199, 174, 165, 184, 179, 130, 137, 148, 159, 70, 77, 80, 91, 106, 97, 124, 119, 30, 21, 8, 3, 50, 57, 36, 47, 141, 134, 155, 144, 161, 170, 183, 188, 213, 222, 195, 200, 249, 242, 239, 228, 61, 54, 43, 32, 17, 26, 7, 12, 101, 110, 115, 120, 73, 66, 95, 84, 247, 252, 225, 234, 219, 208, 205, 198, 175, 164, 185, 178, 131, 136, 149, 158, 71, 76, 81, 90, 107, 96, 125, 118, 31, 20, 9, 2, 51, 56, 37, 46, 140, 135, 154, 145, 160, 171, 182, 189, 212, 223, 194, 201, 248, 243, 238, 229, 60, 55, 42, 33, 16, 27, 6, 13, 100, 111, 114, 121, 72, 67, 94, 85, 1, 10, 23, 28, 45, 38, 59, 48, 89, 82, 79, 68, 117, 126, 99, 104, 177, 186, 167, 172, 157, 150, 139, 128, 233, 226, 255, 244, 197, 206, 211, 216, 122, 113, 108, 103, 86, 93, 64, 75, 34, 41, 52, 63, 14, 5, 24, 19, 202, 193, 220, 215, 230, 237, 240, 251, 146, 153, 132, 143, 190, 181, 168, 163]

gfp13 = [0, 13, 26, 23, 52, 57, 46, 35, 104, 101, 114, 127, 92, 81, 70, 75, 208, 221, 202, 199, 228, 233, 254, 243, 184, 181, 162, 175, 140, 129, 150, 155, 187, 182, 161, 172, 143, 130, 149, 152, 211, 222, 201, 196, 231, 234, 253, 240, 107, 102, 113, 124, 95, 82, 69, 72, 3, 14, 25, 20, 55, 58, 45, 32, 109, 96, 119, 122, 89, 84, 67, 78, 5, 8, 31, 18, 49, 60, 43, 38, 189, 176, 167, 170, 137, 132, 147, 158, 213, 216, 207, 194, 225, 236, 251, 246, 214, 219, 204, 193, 226, 239, 248, 245, 190, 179, 164, 169, 138, 135, 144, 157, 6, 11, 28, 17, 50, 63, 40, 37, 110, 99, 116, 121, 90, 87, 64, 77, 218, 215, 192, 205, 238, 227, 244, 249, 178, 191, 168, 165, 134, 139, 156, 145, 10, 7, 16, 29, 62, 51, 36, 41, 98, 111, 120, 117, 86, 91, 76, 65, 97, 108, 123, 118, 85, 88, 79, 66, 9, 4, 19, 30, 61, 48, 39, 42, 177, 188, 171, 166, 133, 136, 159, 146, 217, 212, 195, 206, 237, 224, 247, 250, 183, 186, 173, 160, 131, 142, 153, 148, 223, 210, 197, 200, 235, 230, 241, 252, 103, 106, 125, 112, 83, 94, 73, 68, 15, 2, 21, 24, 59, 54, 33, 44, 12, 1, 22, 27, 56, 53, 34, 47, 100, 105, 126, 115, 80, 93, 74, 71, 220, 209, 198, 203, 232, 229, 242, 255, 180, 185, 174, 163, 128, 141, 154, 151]

gfp14 = [0, 14, 28, 18, 56, 54, 36, 42, 112, 126, 108, 98, 72, 70, 84, 90, 224, 238, 252, 242, 216, 214, 196, 202, 144, 158, 140, 130, 168, 166, 180, 186, 219, 213, 199, 201, 227, 237, 255, 241, 171, 165, 183, 185, 147, 157, 143, 129, 59, 53, 39, 41, 3, 13, 31, 17, 75, 69, 87, 89, 115, 125, 111, 97, 173, 163, 177, 191, 149, 155, 137, 135, 221, 211, 193, 207, 229, 235, 249, 247, 77, 67, 81, 95, 117, 123, 105, 103, 61, 51, 33, 47, 5, 11, 25, 23, 118, 120, 106, 100, 78, 64, 82, 92, 6, 8, 26, 20, 62, 48, 34, 44, 150, 152, 138, 132, 174, 160, 178, 188, 230, 232, 250, 244, 222, 208, 194, 204, 65, 79, 93, 83, 121, 119, 101, 107, 49, 63, 45, 35, 9, 7, 21, 27, 161, 175, 189, 179, 153, 151, 133, 139, 209, 223, 205, 195, 233, 231, 245, 251, 154, 148, 134, 136, 162, 172, 190, 176, 234, 228, 246, 248, 210, 220, 206, 192, 122, 116, 102, 104, 66, 76, 94, 80, 10, 4, 22, 24, 50, 60, 46, 32, 236, 226, 240, 254, 212, 218, 200, 198, 156, 146, 128, 142, 164, 170, 184, 182, 12, 2, 16, 30, 52, 58, 40, 38, 124, 114, 96, 110, 68, 74, 88, 86, 55, 57, 43, 37, 15, 1, 19, 29, 71, 73, 91, 85, 127, 113, 99, 109, 215, 217, 203, 197, 239, 225, 243, 253, 167, 169, 187, 181, 159, 145, 131, 141]

V_KeyGenerator = ['01', '02', '04', '08', '10', '20', '40', '80', '1b', '36']


#///////////////////////////////////////////////////////auxiliar
def verticalVectors(b):
    matrix = [
        [b[0][0], b[1][0], b[2][0], b[3][0]],
        [b[0][1], b[1][1], b[2][1], b[3][1]],
        [b[0][2], b[1][2], b[2][2], b[3][2]],
        [b[0][3], b[1][3], b[2][3], b[3][3]]
    ]
    return matrix

def horizontalVectors(b):
    matrix = [
        [b[0][0], b[1][0], b[2][0], b[3][0]],
        [b[0][1], b[1][1], b[2][1], b[3][1]],
        [b[0][2], b[1][2], b[2][2], b[3][2]],
        [b[0][3], b[1][3], b[2][3], b[3][3]]
    ]
    return matrix

def subWord(vect):
    tem = [0]*4
    for i in range(4):
        tem[i] = sbox[vect[i]]
    return tem

def four_xor(vect_1, vect_2):
    return [
        vect_1[0] ^ vect_2[0],
        vect_1[1] ^ vect_2[1],
        vect_1[2] ^ vect_2[2],
        vect_1[3] ^ vect_2[3]
    ]

def shift(vect):
    tem = [0]*4
    tem[0]= vect[1]
    tem[1]= vect[2]
    tem[2]= vect[3]
    tem[3]= vect[0]
    return  tem



#///////////////////////////////////////////////////////principales


def addRoundKey(block, key):
    matrix=[
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    for i in range(4):
        for j in range(4):
            matrix[i][j] = block[i][j] ^ key[i][j]
    return matrix

def subBytes(block):
    matrix = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    for i in range(4):
        for j in range(4):
            matrix[i][j] = sbox[block[i][j]]
    return matrix




def shiftRows(b):
    matrix = [
        [b[0][0], b[0][1], b[0][2], b[0][3]],
        [b[1][1], b[1][2], b[1][3], b[1][0]],
        [b[2][2], b[2][3], b[2][0], b[2][1]],
        [b[3][3], b[3][0], b[3][1], b[3][2]]
    ]
    return matrix

def mixx(r):
    matris = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    for i in range(4):
        matris[0][i] = gfp2[r[0][i]] ^ gfp3[r[1][i]] ^ r[2][i] ^ r[3][i]
        matris[1][i] = r[0][i] ^ gfp2[r[1][i]] ^ gfp3[r[2][i]] ^ r[3][i]
        matris[2][i] = r[0][i] ^ r[1][i] ^ gfp2[r[2][i]] ^ gfp3[r[3][i]]
        matris[3][i] = gfp3[r[0][i]] ^ r[1][i] ^ r[2][i] ^ gfp2[r[3][i]]

    return matris



def generateKey(string):
    if len(string) < 16:
        for i in range(16-len(string)):
            string += 'x'
    hexadecimal = [0]*16
    for i in range(len(string)):
        hexadecimal[i] = ord(string[i])

    key = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    cont = 0
    for i in range(4):
        for j in range(4):
            key[i][j] = hexadecimal[cont]
            cont += 1
    return key



def keyGenerator(key):
    actual = key

    llaves = {}
    cont = 1
    cont_v = 0

    for i in range (10):

        vect = actual[3]
        sVector = subWord(shift(vect))
        sVector[0] = sVector[0] ^ int(V_KeyGenerator[cont_v],16)
        cont_v += 1
        newVector_1 = four_xor(sVector, actual[0])
        newVector_2 = four_xor(newVector_1, actual[1])
        newVector_3 = four_xor(newVector_2, actual[2])
        newVector_4 = four_xor(newVector_3, actual[3])

        newKey = [
            newVector_1,
            newVector_2,
            newVector_3,
            newVector_4
        ]
        llaves[cont] = newKey
        cont += 1
        actual = newKey
    return llaves



def encryptBlock(blok, key, originalKey):
    llaves = key

    newBlok = addRoundKey(blok, originalKey)

    for i in range(9):
        temKey = llaves[i+1]
        block_1 = subBytes(newBlok)
        block_2= shiftRows(verticalVectors(block_1))
        block_3 = mixx(block_2)
        block_4 = addRoundKey(horizontalVectors(block_3), temKey)
        newBlok = block_4

    b_1 = subBytes(newBlok)
    b_2 = shiftRows(verticalVectors(b_1))
    b_3 = addRoundKey(horizontalVectors(b_2),llaves[10])
    return b_3


def encryp(mensaje, key):
    originalKey = generateKey(key)

    llaves = keyGenerator(originalKey)
    cont = 0
    numMensajes = 1;
    mansajes = {}

    while cont < len(mensaje):
        matris = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        for i in range(4):
            for j in range(4):
                if cont >= len(mensaje):
                    matris[i][j] = ord('x')
                    cont += 1
                else:
                    matris[i][j] = ord(mensaje[cont])
                    cont += 1
        mansajes[numMensajes] = matris
        numMensajes += 1

    blokes = {}
    for i in range(numMensajes-1):
        blokes[i] = encryptBlock(mansajes[i+1],llaves,originalKey)
    string = ''
    for i in range(numMensajes-1):
        matris = blokes[i]
        for j in range(4):
            for k in range(4):
                #print(str(hex(matris[j][k])))
                sTem = str(hex(matris[j][k])).split('0x')
                if len(sTem[1]) == 1:
                    string += '0'
                    string += sTem[1]
                else:
                    string += sTem[1]
    return string


#/////////////////////////////////////////////////////////decrypt////////////////////////

def invMixx(r):
    matris = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    for i in range(4):
        matris[0][i] = gfp14[r[0][i]] ^ gfp11[r[1][i]] ^ gfp13[r[2][i]] ^ gfp9[r[3][i]]
        matris[1][i] = gfp9[r[0][i]] ^ gfp14[r[1][i]] ^ gfp11[r[2][i]] ^ gfp13[r[3][i]]
        matris[2][i] = gfp13[r[0][i]] ^ gfp9[r[1][i]] ^ gfp14[r[2][i]] ^ gfp11[r[3][i]]
        matris[3][i] = gfp11[r[0][i]] ^ gfp13[r[1][i]] ^ gfp9[r[2][i]] ^ gfp14[r[3][i]]

    return matris

def invShiftRows(b):
    matrix = [
        [b[0][0], b[0][1], b[0][2], b[0][3]],
        [b[1][3], b[1][0], b[1][1], b[1][2]],
        [b[2][2], b[2][3], b[2][0], b[2][1]],
        [b[3][1], b[3][2], b[3][3], b[3][0]]
    ]
    return  matrix

def invSubBytes(block):
    matrix = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    for i in range(4):
        for j in range(4):
            matrix[i][j] = isbox[block[i][j]]
    return matrix


def decryptBlock(block, key, oroginalKey):
    b_1 = addRoundKey(block, key[10])
    newBlock = verticalVectors(b_1)

    nllave = 9
    for i in range(9):
        llave= key[nllave - i]
        block_1 = invShiftRows(newBlock)
        block_2 = invSubBytes(block_1)
        block_3 = addRoundKey(horizontalVectors(block_2), llave)
        block_4 = invMixx(verticalVectors(block_3))
        newBlock = block_4

    b_1 = invShiftRows(newBlock)
    b_2 = invSubBytes(b_1)
    b_3 = addRoundKey(horizontalVectors(b_2), oroginalKey)
    return b_3

def decrypt(mensaje, key):
    originalKey = generateKey(key)

    llaves = keyGenerator(originalKey)
    cont = 1
    numMensajes = 1;
    mansajes = {}

    while cont < len(mensaje):
        matris = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        for i in range(4):
            for j in range(4):
                if cont >= len(mensaje):
                    matris[i][j] = 0
                    cont += 1
                else:
                    a = mensaje[cont-1]
                    b = mensaje[cont]
                    matris[i][j] = int (a+b,16)
                    cont += 2

        mansajes[numMensajes] = matris
        numMensajes += 1

    blokes = {}
    for i in range(numMensajes - 1):
        blokes[i] = decryptBlock(mansajes[i + 1], llaves, originalKey)
    string = ''
    for i in range(numMensajes - 1):
        matris = blokes[i]
        for j in range(4):
            for k in range(4):
                string += chr(matris[j][k])
    return string

"""
/////////////////////////////////////////PRUEBA DE QUE FUNCIONA/////////////////////////
mensaje = "hola mundo142531"
llave = 'a23456asdf423658'

cText = encryp(mensaje, llave)

pText = decrypt(cText, llave)


print(cText)
print(pText)

"""
