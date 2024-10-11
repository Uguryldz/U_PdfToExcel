@echo off
SET NSSM_PATH="nssm.exe"  
SET SERVICE_NAME="U_PdfToExcel"                
SET DISPLAY_NAME="U_PdfToExcel"      
SET DESCRIPTION="PDF dosyalarini Excel formatina cevirmek icin kullanilir."
     
SET EXECUTABLE_PATH="U_PdfToExcel.exe"       

REM Install the service using NSSM
%NSSM_PATH% install %SERVICE_NAME% %EXECUTABLE_PATH%

REM Set the display name
%NSSM_PATH% set %SERVICE_NAME% DisplayName %DISPLAY_NAME%

REM Set the service description
%NSSM_PATH% set %SERVICE_NAME% Description %DESCRIPTION%

REM Start the service
%NSSM_PATH% start %SERVICE_NAME%

echo Service %SERVICE_NAME% has been installed and started.
