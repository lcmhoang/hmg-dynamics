import cv2, numpy as np

def image_pair_generation(img1, img2,flow_mag_1,flow_mag_2,random_perturb=32,cropping_window_size=128):
	'''
	Given two original images of a dynamic scene with a static background (sampled at time t and time t+k),
	generate a pair of training sample with a synthesize ground-truth homography
	:param img1: input image 1 (sampled at time t)
	:param img2: input image 2 (sampled at time t+k)
	:param flow_mag_1: magnitude of optical flow f12 (from image 1 to image 2)
	:param flow_mag_2: magnitude of optical flow f21 (from image 2 to image 1)
	:param random_perturb: default = 32
	:param cropping_window_size: size of the sampled cropping window, default is 128x128
	:return:
	'''
	shape1 = img1.shape
	shape2 = img2.shape
	assert(shape1==shape2)
	h = shape1[0]
	w = shape1[1]

	# ===== in image-1
	cropS = cropping_window_size
	x_topleft = np.random.randint(random_perturb,w-cropS-random_perturb)
	y_topleft = np.random.randint(random_perturb,h-cropS-random_perturb)

	x_topright = x_topleft + cropS
	y_topright = y_topleft

	x_bottomleft = x_topleft
	y_bottomleft = y_topleft + cropS

	x_bottomright = x_topleft + cropS
	y_bottomright = y_topleft + cropS

	tl = (x_topleft,y_topleft)
	tr = (x_topright,y_topright)
	br = (x_bottomright,y_bottomright)
	bl = (x_bottomleft,y_bottomleft)

	rect1=np.array([tl,tr,br,bl],dtype=np.float32)

	# ===== in image-2
	x2_topleft = x_topleft+np.random.rand()*random_perturb*np.random.choice([-1.0,1.0])
	y2_topleft = y_topleft+np.random.rand()*random_perturb*np.random.choice([-1.0,1.0])

	x2_topright= x_topright+np.random.rand()*random_perturb*np.random.choice([-1.0,1.0])
	y2_topright= y_topright+np.random.rand()*random_perturb*np.random.choice([-1.0,1.0])

	x2_bottomleft= x_bottomleft+np.random.rand()*random_perturb*np.random.choice([-1.0,1.0])
	y2_bottomleft= y_bottomleft+np.random.rand()*random_perturb*np.random.choice([-1.0,1.0])

	x2_bottomright= x_bottomright+np.random.rand()*random_perturb*np.random.choice([-1.0,1.0])
	y2_bottomright= y_bottomright+np.random.rand()*random_perturb*np.random.choice([-1.0,1.0])

	tl2 = (x2_topleft,y2_topleft)
	tr2 = (x2_topright,y2_topright)
	br2 = (x2_bottomright,y2_bottomright)
	bl2 = (x2_bottomleft,y2_bottomleft)

	rect2 = np.array([tl2, tr2, br2, bl2],dtype=np.float32)

	# ===== homography
	H = cv2.getPerspectiveTransform(src=rect1,dst=rect2)
	H_inverse = np.linalg.inv(H)

	img2_warped = cv2.warpPerspective(src=img2,M=H_inverse,dsize=(w,h))
	flow_mag_2_warped = cv2.warpPerspective(src=flow_mag_2,M=H_inverse,dsize=(w,h))

	img1_crop        = img1       [y_topleft:y_bottomleft, x_topleft:x_topright]
	img2_warped_crop = img2_warped[y_topleft:y_bottomleft, x_topleft:x_topright]
	flow_mag_1_crop  = flow_mag_1[y_topleft:y_bottomleft, x_topleft:x_topright]
	flow_mag_2_warped_crop  = flow_mag_2_warped[y_topleft:y_bottomleft, x_topleft:x_topright]

	# ===== homography: 4 points
	H_four_points = np.subtract(rect2, rect1)
	crop_rect = rect1

	return img1_crop,img2_warped_crop,H_four_points,crop_rect,flow_mag_1_crop,flow_mag_2_warped_crop

