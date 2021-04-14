import cv2 as cv
import numpy as np
import codecs, json 
import os
from shutil import copyfile

class Account:
    parentdir = "C:/practice"   

    def __init__(self,accountName):
        self.accountName = accountName
        path = os.path.join(self.parentdir,self.accountName)
        if (not os.path.exists(path)):
            os.mkdir(path)
            os.chdir(path)
            print("account created")
        else:
            os.chdir(path)
            print("Account exists. using the existing account")

    def saveImage(self,image_path,image_name,encryption_key):
        copyfile(image_path,os.path.join(self.parentdir,self.accountName,image_name))
        # try block to handle exception
        try:
            # take path of image as a input
            path = os.path.join(self.parentdir,self.accountName,image_name)
            
            # taking encryption key as input
            key = encryption_key
            
            # print path of image file and encryption key that
            # we are using
            print('The path of file : ', path)
            print('Key for encryption : ', key)
            
            # open file for reading purpose
            fin = open(path, 'rb')
            
            # storing image data in variable "image"
            image = fin.read()
            fin.close()
            
            # converting image into byte array to
            # perform encryption easily on numeric data
            image = bytearray(image)

            # performing XOR operation on each value of bytearray
            for index, values in enumerate(image):
                image[index] = values ^ key

            # opening file for writting purpose
            fin = open(path, 'wb')
            
            # writing encrypted data in image
            fin.write(image)
            fin.close()
            print('Encryption Done...')

            
        except Exception:
            print('Error caught : ', Exception.__name__)

            
    def deleteImage(self,image_name):
        file_path = os.path.join(self.parentdir,self.accountName,image_name)
        if os.path.exists(file_path):
            os.remove(file_path)
            print("Image deleted")
        else:
            print("Image does not exist")
    
    def displayImage(self,image_name,decryptionKey):
        file_path = os.path.join(self.parentdir,self.accountName,image_name)
        # try block to handle the exception
        try:
            # take path of image as a input
            path = file_path
            
            # taking decryption key as input
            key = decryptionKey
            
            # print path of image file and decryption key that we are using
            print('The path of file : ', path)
            print('Note : Encryption key and Decryption key must be same.')
            print('Key for Decryption : ', key)
            
            # open file for reading purpose
            fin = open(path, 'rb')
            
            # storing image data in variable "image"
            image = fin.read()
            fin.close()
            
            # converting image into byte array to perform decryption easily on numeric data
            image = bytearray(image)

            # performing XOR operation on each value of bytearray
            for index, values in enumerate(image):
                image[index] = values ^ key

            # opening file for writting purpose
            fin = open(path, 'wb')
            
            # writing decryption data in image
            fin.write(image)
            fin.close()
            print('Decryption Done...')


        except Exception:
            print('Error caught : ', Exception.__name__)

        
        image = cv.imread(file_path)
        cv.imshow(image_name, image)
        cv.waitKey(0) 
        #closing all open windows 
        cv.destroyAllWindows()

        # try block to handle exception
        try:
            # take path of image as a input
            path = file_path
            
            # taking encryption key as input
            key = decryptionKey
            
            # print path of image file and encryption key that
            # we are using
            print('The path of file : ', path)
            print('Key for encryption : ', key)
            
            # open file for reading purpose
            fin = open(path, 'rb')
            
            # storing image data in variable "image"
            image = fin.read()
            fin.close()
            
            # converting image into byte array to
            # perform encryption easily on numeric data
            image = bytearray(image)

            # performing XOR operation on each value of bytearray
            for index, values in enumerate(image):
                image[index] = values ^ key

            # opening file for writting purpose
            fin = open(path, 'wb')
            
            # writing encrypted data in image
            fin.write(image)
            fin.close()
            print('Encryption Done...')

            
        except Exception:
            print('Error caught : ', Exception.__name__)


    
    def renameImage(self,oldname,new_name):
        try:
            os.rename(os.path.join(self.parentdir,self.accountName,oldname),os.path.join(self.parentdir,self.accountName,new_name))
            print("Successfully renamed the image")
        except:
            print("Error in renaming the file. The file might not exist")

    def grayScale(self,image_name,decryptionKey):
        file_path = os.path.join(self.parentdir,self.accountName,image_name)
        # try block to handle the exception
        try:
            # take path of image as a input
            path = file_path
            
            # taking decryption key as input
            key = decryptionKey
            
            # print path of image file and decryption key that we are using
            print('The path of file : ', path)
            print('Note : Encryption key and Decryption key must be same.')
            print('Key for Decryption : ', key)
            
            # open file for reading purpose
            fin = open(path, 'rb')
            
            # storing image data in variable "image"
            image = fin.read()
            fin.close()
            
            # converting image into byte array to perform decryption easily on numeric data
            image = bytearray(image)

            # performing XOR operation on each value of bytearray
            for index, values in enumerate(image):
                image[index] = values ^ key

            # opening file for writting purpose
            fin = open(path, 'wb')
            
            # writing decryption data in image
            fin.write(image)
            fin.close()
            print('Decryption Done...')


        except Exception:
            print('Error caught : ', Exception.__name__)

        
        img = cv.imread(file_path)

        gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        cv.imshow('Gray',gray)
        cv.waitKey(0) 
        #closing all open windows 
        cv.destroyAllWindows()

        # try block to handle exception
        try:
            # take path of image as a input
            path = file_path
            
            # taking encryption key as input
            key = decryptionKey
            
            # print path of image file and encryption key that
            # we are using
            print('The path of file : ', path)
            print('Key for encryption : ', key)
            
            # open file for reading purpose
            fin = open(path, 'rb')
            
            # storing image data in variable "image"
            image = fin.read()
            fin.close()
            
            # converting image into byte array to
            # perform encryption easily on numeric data
            image = bytearray(image)

            # performing XOR operation on each value of bytearray
            for index, values in enumerate(image):
                image[index] = values ^ key

            # opening file for writting purpose
            fin = open(path, 'wb')
            
            # writing encrypted data in image
            fin.write(image)
            fin.close()
            print('Encryption Done...')

            
        except Exception:
            print('Error caught : ', Exception.__name__)

    def labscale(self,image_name,decryptionKey):
        file_path = os.path.join(self.parentdir,self.accountName,image_name)
        # try block to handle the exception
        try:
            # take path of image as a input
            path = file_path
            
            # taking decryption key as input
            key = decryptionKey
            
            # print path of image file and decryption key that we are using
            print('The path of file : ', path)
            print('Note : Encryption key and Decryption key must be same.')
            print('Key for Decryption : ', key)
            
            # open file for reading purpose
            fin = open(path, 'rb')
            
            # storing image data in variable "image"
            image = fin.read()
            fin.close()
            
            # converting image into byte array to perform decryption easily on numeric data
            image = bytearray(image)

            # performing XOR operation on each value of bytearray
            for index, values in enumerate(image):
                image[index] = values ^ key

            # opening file for writting purpose
            fin = open(path, 'wb')
            
            # writing decryption data in image
            fin.write(image)
            fin.close()
            print('Decryption Done...')


        except Exception:
            print('Error caught : ', Exception.__name__)

        
        img = cv.imread(file_path)

        gray = cv.cvtColor(img,cv.COLOR_BGR2LAB)
        cv.imshow('Gray',gray)
        cv.waitKey(0) 
        #closing all open windows 
        cv.destroyAllWindows()

        # try block to handle exception
        try:
            # take path of image as a input
            path = file_path
            
            # taking encryption key as input
            key = decryptionKey
            
            # print path of image file and encryption key that
            # we are using
            print('The path of file : ', path)
            print('Key for encryption : ', key)
            
            # open file for reading purpose
            fin = open(path, 'rb')
            
            # storing image data in variable "image"
            image = fin.read()
            fin.close()
            
            # converting image into byte array to
            # perform encryption easily on numeric data
            image = bytearray(image)

            # performing XOR operation on each value of bytearray
            for index, values in enumerate(image):
                image[index] = values ^ key

            # opening file for writting purpose
            fin = open(path, 'wb')
            
            # writing encrypted data in image
            fin.write(image)
            fin.close()
            print('Encryption Done...')

            
        except Exception:
            print('Error caught : ', Exception.__name__)
        
    def hsvScale(self,image_name,decryptionKey):
        file_path = os.path.join(self.parentdir,self.accountName,image_name)
        # try block to handle the exception
        try:
            # take path of image as a input
            path = file_path
            
            # taking decryption key as input
            key = decryptionKey
            
            # print path of image file and decryption key that we are using
            print('The path of file : ', path)
            print('Note : Encryption key and Decryption key must be same.')
            print('Key for Decryption : ', key)
            
            # open file for reading purpose
            fin = open(path, 'rb')
            
            # storing image data in variable "image"
            image = fin.read()
            fin.close()
            
            # converting image into byte array to perform decryption easily on numeric data
            image = bytearray(image)

            # performing XOR operation on each value of bytearray
            for index, values in enumerate(image):
                image[index] = values ^ key

            # opening file for writting purpose
            fin = open(path, 'wb')
            
            # writing decryption data in image
            fin.write(image)
            fin.close()
            print('Decryption Done...')


        except Exception:
            print('Error caught : ', Exception.__name__)

        
        img = cv.imread(file_path)

        gray = cv.cvtColor(img,cv.COLOR_BGR2HSV)
        cv.imshow('Gray',gray)
        cv.waitKey(0) 
        #closing all open windows 
        cv.destroyAllWindows()

        # try block to handle exception
        try:
            # take path of image as a input
            path = file_path
            
            # taking encryption key as input
            key = decryptionKey
            
            # print path of image file and encryption key that
            # we are using
            print('The path of file : ', path)
            print('Key for encryption : ', key)
            
            # open file for reading purpose
            fin = open(path, 'rb')
            
            # storing image data in variable "image"
            image = fin.read()
            fin.close()
            
            # converting image into byte array to
            # perform encryption easily on numeric data
            image = bytearray(image)

            # performing XOR operation on each value of bytearray
            for index, values in enumerate(image):
                image[index] = values ^ key

            # opening file for writting purpose
            fin = open(path, 'wb')
            
            # writing encrypted data in image
            fin.write(image)
            fin.close()
            print('Encryption Done...')

            
        except Exception:
            print('Error caught : ', Exception.__name__)

    def xyzScale(self,image_name,decryptionKey):
        file_path = os.path.join(self.parentdir,self.accountName,image_name)
        # try block to handle the exception
        try:
            # take path of image as a input
            path = file_path
            
            # taking decryption key as input
            key = decryptionKey
            
            # print path of image file and decryption key that we are using
            print('The path of file : ', path)
            print('Note : Encryption key and Decryption key must be same.')
            print('Key for Decryption : ', key)
            
            # open file for reading purpose
            fin = open(path, 'rb')
            
            # storing image data in variable "image"
            image = fin.read()
            fin.close()
            
            # converting image into byte array to perform decryption easily on numeric data
            image = bytearray(image)

            # performing XOR operation on each value of bytearray
            for index, values in enumerate(image):
                image[index] = values ^ key

            # opening file for writting purpose
            fin = open(path, 'wb')
            
            # writing decryption data in image
            fin.write(image)
            fin.close()
            print('Decryption Done...')


        except Exception:
            print('Error caught : ', Exception.__name__)

        
        img = cv.imread(file_path)

        gray = cv.cvtColor(img,cv.COLOR_BGR2XYZ)
        cv.imshow('Gray',gray)
        cv.waitKey(0) 
        #closing all open windows 
        cv.destroyAllWindows()

        # try block to handle exception
        try:
            # take path of image as a input
            path = file_path
            
            # taking encryption key as input
            key = decryptionKey
            
            # print path of image file and encryption key that
            # we are using
            print('The path of file : ', path)
            print('Key for encryption : ', key)
            
            # open file for reading purpose
            fin = open(path, 'rb')
            
            # storing image data in variable "image"
            image = fin.read()
            fin.close()
            
            # converting image into byte array to
            # perform encryption easily on numeric data
            image = bytearray(image)

            # performing XOR operation on each value of bytearray
            for index, values in enumerate(image):
                image[index] = values ^ key

            # opening file for writting purpose
            fin = open(path, 'wb')
            
            # writing encrypted data in image
            fin.write(image)
            fin.close()
            print('Encryption Done...')

            
        except Exception:
            print('Error caught : ', Exception.__name__)