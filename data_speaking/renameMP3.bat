@echo off
setlocal enabledelayedexpansion

rem Yêu cầu người dùng nhập số lượng file cần đổi tên
set /p num_files="Nhap so luong: "

for /L %%i in (1,1,%num_files%) do (
    ren "output_%%i.mp3" "%%i.mp3"
)

endlocal