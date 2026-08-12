"""
大乐透智能分析投注助手 - 本地服务器
同时提供静态文件服务和 API 代理，解决浏览器 CORS 限制
仅使用 Python 内置模块，无需额外安装
"""
import http.server
import urllib.request
import urllib.error
import json
import os
import sys
import ssl
import io

# 修复 Windows GBK 编码问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

PORT = 8080
API_BASE = "https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry"


class ProxyHandler(http.server.SimpleHTTPRequestHandler):
    """静态文件 + API 代理处理器"""

    def do_GET(self):
        # API 代理路径: /api/lottery?pageNo=1&pageSize=30
        if self.path.startswith("/api/lottery"):
            self.proxy_api()
        # 默认首页
        elif self.path == "/" or self.path == "":
            self.path = "/index.html"
            super().do_GET()
        else:
            super().do_GET()

    def proxy_api(self):
        """代理请求到体彩官方 API"""
        try:
            # 解析查询参数
            query_str = self.path.split("?", 1)[1] if "?" in self.path else ""
            url = f"{API_BASE}?{query_str}"

            req = urllib.request.Request(url)
            req.add_header("User-Agent",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
            req.add_header("Accept", "application/json")
            req.add_header("Referer", "https://www.lottery.gov.cn/")

            # 忽略 SSL 证书验证（某些环境可能需要）
            ctx = ssl.create_default_context()

            with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
                data = resp.read()
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.send_header("Cache-Control", "max-age=300")
                self.end_headers()
                self.wfile.write(data)

        except urllib.error.HTTPError as e:
            self.send_error(e.code, f"API Error: {e.reason}")
        except Exception as e:
            self.send_error(502, f"代理请求失败: {str(e)}")

    def do_OPTIONS(self):
        """处理 CORS 预检请求"""
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.end_headers()

    def log_message(self, format, *args):
        """自定义日志格式"""
        if "/api/lottery" in str(args[0]):
            print(f"  [>>] {args[0]}")
        else:
            pass  # 静默静态文件请求


def main():
    # 切换到脚本所在目录
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    print("""
  ====================================
    大乐透智能分析投注助手
    本地服务器启动中...
  ====================================
    """)

    server = http.server.HTTPServer(("0.0.0.0", PORT), ProxyHandler)

    print(f"  [OK] 服务已启动: http://localhost:{PORT}")
    print(f"  [*] 手机访问: http://<你的电脑IP>:{PORT}")
    print(f"  [!] 按 Ctrl+C 停止服务")
    print(f"  ----------------------------------")
    print()

    # 自动打开浏览器
    import webbrowser
    webbrowser.open(f"http://localhost:{PORT}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\n  已停止服务。再见！")
        server.shutdown()


if __name__ == "__main__":
    main()
