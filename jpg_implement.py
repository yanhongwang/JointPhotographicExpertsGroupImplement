#!/usr/bin/python -d

from math import *

subblock=[   50,  52,  57,   59,   61,   83,   79,   75],\
    [   51,  49,  56,   60,   68,   80,   75,   70],\
    [   67,  75,  90,   102,    119,  111,  88,   72],\
    [   58,  59,  75,   88,   113,   104,   91,   75],\
    [   67,  64,  69,   93,   99,   85,  84,   62],\
    [   69,  70,  73,   65,   80,   71,   73,   76],\
    [   78,  74,  71,   70,   66,   69,   72,   78],\
    [   70,  68,  72,   80,   81,   68,   66,   64];


for i in range( 0, 8 ):
	for  k  in  range( 0, 8 ):
		print subblock[ i ][ k ],
	print				

print
print "(a)Subblock of Original Image"
print


for i in range( 0, 8 ):
	for  k  in  range( 0, 8 ):
		subblock[ i ][ k ] -= 128
		print subblock[ i ][ k ],
	print

print
print "(b)After gray Scale Level Shift"
print


normalized_matrix=[   0,   0,  0,   0,   0,   0,   0,   0],\
              [  0,0,  0,   0,   0,   0,   0,   0],\
	      [  0,  0,  0,   0,   0,   0,0,    0],\
	      [   0,  0,  0,   0,   0,   0,   0,   0],\
	      [  0,0,  0,   0,   0,   0,   0,   0],\
	      [  0,  0,  0,   0,   0,   0,0,    0],\
	      [   0,  0,  0,   0,   0,   0,   0,   0],\
	      [  0,0,  0,   0,   0,   0,   0,   0];

normalization_matrix=[  128,  88,  80,  128, 192, 320, 408, 488],\
       [ 96, 96, 112, 152, 208, 464, 480, 440],\
       [ 112,  104,  128,  192,  320,456,  552,  448],\
       [ 112, 136, 176, 232, 408, 696, 640, 496],\
       [ 144, 176, 296, 448, 544, 872, 824, 616],\
       [ 192,  280,  440,512,  648,  832,  904,  736],\
       [ 392, 512, 624, 696, 824, 968,960, 808],\
       [ 576, 736, 760, 784, 896, 800, 824, 792]

total = 0


for i in range( 0, 8 ):
	for k in range( 0, 8 ):
		for m in range( 0, 8 ):
			for n in range( 0, 8 ):
				total+=subblock[m][n]*cos((2*m+1)*i*pi/16)\
				* cos(  ( 2 * n + 1) * k * pi / 16 )
		normalized_matrix[i][k]  =  round( total * 4 / normalization_matrix[ i][ k ], 0 )
		print round( total * 4, 0 ),
		total = 0
	print

print
print "(c)Discrete Cosine Transform"
print

for i in range( 0, 8 ):
	for k in range( 0, 8 ):
		print normalization_matrix[ i ][ k ],
	print

print
print "(d)A Normalization Matrix"
print



for i in range( 0, 8 ):
	for  k  in  range(  0,  8  ):
		print normalized_matrix[i][k],
	print

print
print "(e)Normalized Matrix"
print

total = 0

for m in range( 0, 8 ):
	for n in range( 0, 8 ):
		normalized_matrix[m][n] *= normalization_matrix[ m ][ n ]
		print normalized_matrix[ m ][ n ],
	print

print
print "Recoveried Matrix"
print


for m in range( 0, 8 ):
	for n in range( 0, 8 ):
		for i in range( 0, 8 ):
			for k in range( 0, 8 ):
				if i == 0:
					b1 = 0.5
				else:
					b1 = 1
				
				if k == 0:
					b2 = 0.5
				else:
					b2 = 1
				total+=b1*b2*normalized_matrix[i][k]*cos((2*m+1)\
				* i * pi/ 16 )*cos( ( 2 * n + 1 ) * k*pi/16)
		
		subblock[m][n]=total / 64
		print round( subblock[m][n] + 128, 0 ),
		total = 0
	print
	
print
print "(h)Reconstructed Subblock"
print

