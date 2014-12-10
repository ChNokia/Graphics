# -*- coding: utf-8 -*- 

import os.path

import PythonMagick

def str_to_real_size(str_size):
	real_size = str_size.split('x')

	return [int(data) for data in real_size]

def multiresize(entity, id):
	inputFilePathTemplate  = 'images/%s/%s/original.jpeg'
	outputFilePathTemplate = 'images/%s/%s/%s@%sx.jpeg'

	inputFile = inputFilePathTemplate % (entity, id)

	if not os.path.exists(inputFile):
		raise ValueError('No exists file!')

	densities = [1, 1.5, 2]
   	jpeg_qualities = {'1' : 80,
   					'1.5' : 60,
   					'2' : 40
   					}
   	image_sizes = {
   				'article' : ['100x75', '600x450'],
   				'category' : ['100x75', '200x150']
   				}

	for image_size in image_sizes['article']:
		real_size = str_to_real_size(image_size)

		for densitie in densities:
			new_size = map((lambda x: int(x * densitie)), real_size)
			new_image = PythonMagick.Image(inputFile)

			new_image.sample('!{0}x{1}'.format(new_size[0], new_size[1]))
			new_image.quality(jpeg_qualities[str(densitie)])
			new_image.write((outputFilePathTemplate % (entity, id, image_size, densitie)))

def main():
	multiresize('article', 42)

if __name__ == '__main__':
	main()