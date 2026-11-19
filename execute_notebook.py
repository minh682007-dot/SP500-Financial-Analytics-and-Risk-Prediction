import nbformat
from nbformat.v4 import new_output
import sys
import io
import contextlib
import traceback

print("🔄 Đang nạp notebook tieuluan.ipynb...")
with open('tieuluan.ipynb', 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

global_env = {}

total_code = sum(1 for c in nb.cells if c.cell_type == 'code')
print(f"Tổng số code cells cần chạy: {total_code}")

code_idx = 0
for idx, cell in enumerate(nb.cells):
    if cell.cell_type == 'code':
        code_idx += 1
        code_str = ''.join(cell.source)
        print(f"[{code_idx}/{total_code}] Đang chạy cell {idx+1}...", end=' ')
        
        stdout_buf = io.StringIO()
        cell.outputs = []
        cell.execution_count = code_idx
        
        def custom_display(*args):
            for a in args:
                if hasattr(a, 'to_string'):
                    stdout_buf.write(a.to_string() + "\n")
                elif hasattr(a, 'to_html'):
                    stdout_buf.write(a.to_string() + "\n")
                else:
                    stdout_buf.write(str(a) + "\n")
        
        global_env['display'] = custom_display
        
        try:
            with contextlib.redirect_stdout(stdout_buf), contextlib.redirect_stderr(stdout_buf):
                exec(code_str, global_env)
            
            out_text = stdout_buf.getvalue()
            if out_text:
                cell.outputs.append(new_output(
                    output_type='stream',
                    name='stdout',
                    text=out_text
                ))
            print("✓ OK")
        except Exception as e:
            err_msg = traceback.format_exc()
            cell.outputs.append(new_output(
                output_type='error',
                ename=type(e).__name__,
                evalue=str(e),
                traceback=err_msg.split('\n')
            ))
            print(f"❌ LỖI: {e}")
            break

with open('tieuluan.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

print("🎉 ĐÃ HOÀN TẤT THỰC THI VÀ LƯU TOÀN BỘ KẾT QUẢ ĐẦU RA VÀO tieuluan.ipynb!")
