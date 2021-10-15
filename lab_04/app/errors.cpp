//
// Created by ivaaahn on 14.10.2021.
//

#include "errors.hpp"
#include <string>

std::string err_handler(const err_t code) {
    switch (code) {
        case ERR_FOPEN:
            return "Не удалось открыть файл!";
        case ERR_FREAD:
            return "Не удалось считать файл!";
        case ERR_POINTS_QTY:
            return "Некорректное количество точек!";
        case ERR_MEM:
            return "Произошла ошибка при обращении к данным!";
        case ERR_ALLOC:
            return "Произошла ошибка при выделении памяти";
        case ERR_ARGV:
            return "Не указано имя файла, содержащего модель!";
        default:
            return "Неизвестная ошибка";
    }
}