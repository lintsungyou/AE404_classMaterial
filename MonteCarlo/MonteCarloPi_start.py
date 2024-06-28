import random

TOTAL_POINTS =  #總共要撒的點的數目，越高計算得越準但計算時間越長
RADIUS =  #正方形半徑，越高邊界影響越小，太低會影響準度

#儲存X座標的 LIST
#儲存Y座標的LIST
#points in the circle  在圓內的點的數目


#步驟三： 隨機在測試圖面半徑的範圍內產生x,y 座標 並存入xs[], ys[]中，總共需要產生TOTAL_POINTS個x, y座標


#步驟四，利用 x^2 + y^2 < R^2 的條件檢驗產生的點是否在扇形之內



#步驟五：利用扇形內的點代表扇形面積，全部的點代表正方形面積，並計算出PI 的估計值
monteCarloPi = 

print("pi: " + str(monteCarloPi))