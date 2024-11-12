import cv2
import numpy as np


def correct_perspective(image):
    # 透视变换步骤，假设你已经知道四个角点的坐标
    pts1 = np.float32([[50, 50], [200, 50], [50, 200], [200, 200]])  # 示例角点
    pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    corrected_image = cv2.warpPerspective(image, matrix, (300, 300))
    return corrected_image


def adaptive_histogram_equalization(image):
    # 自适应直方图均衡化
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    equalized_image = clahe.apply(image)
    return equalized_image


def extract_text_contours(image):
    # 图像形态操作 1: 提取文本轮廓
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    edged = cv2.Canny(blurred, 50, 150)
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours


def create_text_mask(image, contours):
    # 创建白色背景掩模
    mask = np.ones(image.shape, dtype=np.uint8) * 255
    cv2.drawContours(mask, contours, -1, (0, 0, 0), -1)
    return mask


def poisson_image_fusion(image, mask):
    # Poisson 图像融合
    center = (image.shape[1] // 2, image.shape[0] // 2)
    fusion_image = cv2.seamlessClone(image, mask, mask, center, cv2.NORMAL_CLONE)
    return fusion_image


def process_image(image_path):
    # 读取图像
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 校正透视变换
    corrected_image = correct_perspective(image)

    # 自适应直方图均衡化
    equalized_image = adaptive_histogram_equalization(corrected_image)

    # 提取文本轮廓
    contours = extract_text_contours(equalized_image)

    # 创建文本掩模
    text_mask = create_text_mask(equalized_image, contours)

    # Poisson 图像融合
    final_image = poisson_image_fusion(equalized_image, text_mask)

    # 对最终图像进行自适应直方图均衡化
    final_image_equalized = adaptive_histogram_equalization(final_image)

    return final_image_equalized


# 示例图像路径
image_path = 'path/to/your/image.jpg'
processed_image = process_image(image_path)

# 显示结果
cv2.imshow('Processed Image', processed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()