
library(readxl)  #чтение из excel
library(dplyr)  #современные средства программирования, включая функциональное
library(ggplot2)  #красивые удобные графики
library(ggpubr)  #группировка изображений
library(corrplot)  #картинка для корреляционной матрицы
library(psych)  #факторный анализ
library(MASS)  #линейный дискриминантный анализ
library(tree)  #визуализация деревьев
library(randomForest)  #случайные леса
library(TeachingDemos)  #пиктограммы
library(mice)  #обработка отсутствующих значений
library(corrgram)  #коррелограммы
library(magrittr)  #конвеерный оператор
library(plotly)  #интерактивная графика
library(factoextra)  #графика по главным компонентам

library(tidyverse)

setwd('C:/Users/qtckp/OneDrive/Рабочий стол/SberHak/word2vec')

data = read_csv('w2v.csv', col_types = c(col_character(),rep(col_double(), 32)))

colnames(data)[1] = 'words'

data[, 2:33] = apply(data[, 2:33], 2, function(x) scale(as.numeric(x)))



d = dist(data[, 2:33], method = "euclidean")

fit <- hclust(d, method = "ward.D")

plot(fit, labels = data$words, xlab = "words")

plot(fit$height[2900:length(fit$height)], xlab = "step", ylab = "dist", type = "b", col = "blue", lwd = 1, 
     main = "Расстояния при объединении кластеров")




it = 1:50
sums = sapply(it, function(k) kmeans(data[, 2:33], k)$tot.withinss)
plot(it, sums, type = "b", col = "red", main = "Суммы внутригрупповых расстояний при разном числе кластеров")




fit = kmeans(data[, 2:33], 30, algorithm = c("MacQueen"), trace=TRUE)

library(factoextra)
print(fviz_cluster(fit, data[, -1], ellipse.type = "norm", geom = 'text'))




