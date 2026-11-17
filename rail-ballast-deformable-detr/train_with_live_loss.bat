@echo off
setlocal
cd /d "%~dp0"

rem First optional argument is the output directory (default: output_live).
rem This avoids mixing a new run with the existing output/log.txt.
set "OUTDIR=%~1"
if "%OUTDIR%"=="" set "OUTDIR=output_live"

echo Starting Deformable DETR training in a new window...
echo Output directory: %OUTDIR%
start "Deformable DETR Training" python train_deformable_detr.py --output_dir "%OUTDIR%"

echo Starting live loss viewer...
echo Log file: %OUTDIR%\log.txt
python tools\live_loss_matplotlib.py --log "%OUTDIR%\log.txt"

endlocal
