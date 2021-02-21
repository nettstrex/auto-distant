#created by NETTSTREX
import os
import sys
import time
import json
import getpass
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
path = f'C:\\Users\\{getpass.getuser()}\\AppData\\Roaming\\auto-distant'
optian = webdriver.ChromeOptions()
optian.headless = False
optian.add_argument('--use-fake-ui-for-media-stream')
time_now = str(datetime.datetime.now().time().hour) + ':' + str(datetime.datetime.now().time().minute)
file = os.getcwd() + '\\' + __file__.strip('.py') + '.exe' #в exe файле переменная __file__ не содержит путь к файлу
def xml(user_data):
	lesson_time = list(user_data['schedule'].keys())
	f = open('task.xml', 'w')
	f.write(f'''<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo>
    <Date>2021-02-18T14:57:57.2783359</Date>
    <Author>DESKTOP-NJFOES6\\{getpass.getuser()}</Author>
    <URI>\\Расписание</URI>
  </RegistrationInfo>
  <Triggers>
    <CalendarTrigger>
      <StartBoundary>2021-02-18T{lesson_time[0]}:00</StartBoundary>
      <Enabled>true</Enabled>
      <ScheduleByDay>
        <DaysInterval>1</DaysInterval>
      </ScheduleByDay>
    </CalendarTrigger>
    <CalendarTrigger>
      <StartBoundary>2021-02-18T{lesson_time[1]}:00</StartBoundary>
      <Enabled>true</Enabled>
      <ScheduleByDay>
        <DaysInterval>1</DaysInterval>
      </ScheduleByDay>
    </CalendarTrigger>
    <CalendarTrigger>
      <StartBoundary>2021-02-18T{lesson_time[2]}:00</StartBoundary>
      <Enabled>true</Enabled>
      <ScheduleByDay>
        <DaysInterval>1</DaysInterval>
      </ScheduleByDay>
    </CalendarTrigger>
    <CalendarTrigger>
      <StartBoundary>2021-02-18T{lesson_time[3]}:00</StartBoundary>
      <Enabled>true</Enabled>
      <ScheduleByDay>
        <DaysInterval>1</DaysInterval>
      </ScheduleByDay>
    </CalendarTrigger>
    <CalendarTrigger>
      <StartBoundary>2021-02-18T{lesson_time[4]}:00</StartBoundary>
      <Enabled>true</Enabled>
      <ScheduleByDay>
        <DaysInterval>1</DaysInterval>
      </ScheduleByDay>
    </CalendarTrigger>
    <CalendarTrigger>
      <StartBoundary>2021-02-18T{lesson_time[5]}:00</StartBoundary>
      <Enabled>true</Enabled>
      <ScheduleByDay>
        <DaysInterval>1</DaysInterval>
      </ScheduleByDay>
    </CalendarTrigger>
    <CalendarTrigger>
      <StartBoundary>2021-02-18T{lesson_time[6]}:00</StartBoundary>
      <Enabled>true</Enabled>
      <ScheduleByDay>
        <DaysInterval>1</DaysInterval>
      </ScheduleByDay>
    </CalendarTrigger>
  </Triggers>
  <Principals>
    <Principal id="Author">
      <UserId>S-1-5-21-1082988689-3211238964-3685127817-1002</UserId>
      <LogonType>InteractiveToken</LogonType>
      <RunLevel>HighestAvailable</RunLevel>
    </Principal>
  </Principals>
  <Settings>
    <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>true</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>false</StopIfGoingOnBatteries>
    <AllowHardTerminate>false</AllowHardTerminate>
    <StartWhenAvailable>true</StartWhenAvailable>
    <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable>
    <IdleSettings>
      <StopOnIdleEnd>true</StopOnIdleEnd>
      <RestartOnIdle>false</RestartOnIdle>
    </IdleSettings>
    <AllowStartOnDemand>true</AllowStartOnDemand>
    <Enabled>false</Enabled>
    <Hidden>false</Hidden>
    <RunOnlyIfIdle>false</RunOnlyIfIdle>
    <WakeToRun>true</WakeToRun>
    <ExecutionTimeLimit>PT72H</ExecutionTimeLimit>
    <Priority>7</Priority>
  </Settings>
  <Actions Context="Author">
    <Exec>
      <Command>{file}</Command>
    </Exec>
  </Actions>
</Task>
	''')

def config():
	if not os.path.isdir(path):
		print('НЕ ЗАБУДЬТЕ ДОБАВИТЬ TASK.XML В ПАЛНИРОВЩИК ЗАДАЧ!')
		login = input('Введите логин от дневника: ')
		password = input('Введите пароль от дневника: ')
		name = input('Введите ваше имя, которе будет отображаться при входе в teems: ')
		schedule = {}
		for i in range(1, 8):
			user_time = input(f'Введите когда у вас начинаеться {i}й урок: ')
			if len(user_time) == 4:
				user_time = '0' + user_time
			schedule[user_time] = str(i)
		user_data = {'login' : login, 'password' : password, 'name' : name, 'schedule' : schedule }
		os.mkdir(path)
		f = open(path + '\\config.ini', 'w')
		json.dump(user_data, f)
		xml(user_data)
	else:
		f = open(path + '\\config.ini', 'r', encoding='utf-8')
		js = f.read()
		user_data = json.loads(js)
		return user_data

def authorization():
	global browser
	browser = webdriver.Chrome(options=optian)
	browser.get('https://dnevnik.mos.ru/')
	browser.find_element_by_xpath('/html/body/ui-view/div/div[1]/div/div[2]/div[1]/a').click()
	time.sleep(1)
	browser.find_element_by_xpath('/html/body/div[1]/section/section/div[2]/form/div[1]/div/div/input').send_keys(config()['login'])
	time.sleep(1)
	browser.find_element_by_xpath('/html/body/div[1]/section/section/div[2]/form/div[2]/div/input').send_keys(config()['password'])
	time.sleep(1)
	browser.find_element_by_xpath('/html/body/div[1]/section/section/div[2]/form/button').click()
	time.sleep(5)
	browser.get('https://dnevnik.mos.ru/student_diary/student_diary/15519823')
	time.sleep(15)

def lesson_click():
	weekday = datetime.datetime.today().weekday()+1
	lesson = config()['schedule'][time_now]
	browser.find_element_by_xpath(f'/html/body/diary-root/ezd-main-layout/div/section/ezd-base-layout/section/div/div[2]/div[1]/diary-student-diary-content/div/div/diary-student-diary-day[{weekday}]/div/div[2]/div[{lesson}]').click()
	time.sleep(0.5)
	browser.find_element_by_xpath('/html/body/diary-root/ezd-main-layout/div/section/ezd-base-layout/section/div/div[2]/div[1]/diary-student-diary-content/div/diary-student-diary-lesson-detail-panel/div/div[2]/div[1]/button').click()
	time.sleep(2)

def teems():
	window_before = browser.window_handles[1]
	browser.close()
	browser.switch_to_window(window_before)
	browser.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div[3]/button[2]').click()
	time.sleep(5)
	browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[1]/div/button/span[1]').click()
	browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[2]/div/button/span[1]').click()
	browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div[1]/input').send_keys(config()['name'])
	browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div[2]/button').click()

if __name__ == '__main__':
	print('Прога работает нормально, спи спокойно)')
	config()
	authorization()
	lesson_click()
	teems()
