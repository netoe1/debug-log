#include <stdio.h>
#include <stdbool.h>
#include <time.h>
#include <stdarg.h>

bool debug_ativado = true;

// Cores ANSI (Estilo ts-node)
#define COLOR_RESET   "\033[0m"
#define COLOR_GRAY    "\033[90m"
#define COLOR_GREEN   "\033[32m"
#define COLOR_CYAN    "\033[36m"
#define COLOR_YELLOW  "\033[33m"
#define COLOR_RED     "\033[31m"
#define COLOR_BLUE    "\033[34m" // Azul escuro

void console_log_impl(const char *level, const char *level_color, const char *file, int line, const char *fmt, ...) {
    time_t rawtime;
    struct tm *timeinfo;
    char time_buf[20];
    time(&rawtime);
    timeinfo = localtime(&rawtime);
    strftime(time_buf, sizeof(time_buf), "%H:%M:%S", timeinfo);

    // Bloco do nível: [LOG], [INFO], [WARN], [DEBUG], [ERROR]
    char level_buf[12];
    snprintf(level_buf, sizeof(level_buf), "[%s]", level);

    // Bloco do arquivo + linha com dois pontos colados: [Console.c:50]:
    char location_buf[36];
    snprintf(location_buf, sizeof(location_buf), "[%s:%d]:", file, line);

    // Formatação alinhada em colunas
    printf("%s%-9s%s %s%s%s %s%-18s" COLOR_RESET " ", 
           level_color, level_buf, COLOR_RESET, 
           COLOR_GRAY, time_buf, COLOR_RESET, 
           COLOR_GRAY, location_buf);

    va_list args;
    va_start(args, fmt);
    vprintf(fmt, args);
    va_end(args);

    printf(";\n");
}

// Macros públicas
#define ConsoleLog(...)   console_log_impl("LOG",   COLOR_GREEN,   __FILE__, __LINE__, __VA_ARGS__)
#define ConsoleInfo(...)  console_log_impl("INFO",  COLOR_CYAN,    __FILE__, __LINE__, __VA_ARGS__)
#define ConsoleWarn(...)  console_log_impl("WARN",  COLOR_YELLOW,  __FILE__, __LINE__, __VA_ARGS__)
#define ConsoleError(...) console_log_impl("ERROR", COLOR_RED,     __FILE__, __LINE__, __VA_ARGS__)

#define ConsoleDebug(...) \
    do { \
        if (debug_ativado) { \
            console_log_impl("DEBUG", COLOR_BLUE, __FILE__, __LINE__, __VA_ARGS__); \
        } \
    } while(0)

int main(void) {
    ConsoleLog("Aplicação inicializada com sucesso");
    ConsoleInfo("Servidor escutando na porta 3000");
    ConsoleWarn("Uso de memória acima de 80%%");
    ConsoleDebug("Objeto de contexto carregado na memória");
    ConsoleError("Conexão interrompida pelo host");

    return 0;
}