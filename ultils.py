from os import listdir

def product_pic_dict(PRODUCTS_DIR):

		return {
		    product_name: product_name.split(".")[1]
		    for product_name in listdir(PRODUCTS_DIR)
		}