# -*- coding: utf-8 -*-



class MessageBox:

	def __init__ (self, mMessage):
		session.flash = mMessage
		pass

	def showWarning(self):
		response.mMessageBox_Theme = "warning"
		response.mMessageBox_Icon  = "glyphicon glyphicon-warning-sign"
		response.mShowed = False
		pass

	def showSuccess(self):
		response.mMessageBox_Theme = "success"
		response.mMessageBox_Icon  = "glyphicon glyphicon-ok-circle"
		pass

	def showError(self):
		response.mMessageBox_Theme = "danger"
		response.mMessageBox_Icon  = "glyphicon glyphicon-remove-circle"
		pass

	def showInfo(self):
		response.mMessageBox_Theme = "info"
		response.mMessageBox_Icon  = "glyphicon glyphicon-info-sign"
		pass

	def setTimer(mTimer):
		try:
			response.mMessageBox_Timer = int(mTimer)
		except:
			response.mMessageBox_Timer = 4000
		pass

	def resetTimer():
		response.mMessageBox_Timer = 4000
		pass



class MyApplication:

    def __init__(self):
		self.KEY_CONNECTION = "46213fdsfc5f6523d698ca5af2r356gs59c4fd321843813e4cbadasd"
		pass

    def isValidKey(self):
		try:
			return request.vars.mKey == self.KEY_CONNECTION
		except:
			pass

		return False

     #Get all items of wallet filtering if it is an inflow or an outflow.
    def getFirstYearDeviceConnectionTable(self, mId):
 	    #maxID=db(db.tbDeviceConnection.mDevice == mDevice.id).select(db.tbDeviceConnection.id.max()).first()[db.tbDeviceConnection.id.max()]
 	    mRow = db.tbDeviceConnection(mDevice = mId)

 	    if mRow == None:
 	        return request.now.year
 	    else:
 	        return mRow.mDateTime.year


    #Check if device exists.
    def isDeviceAcceptableByMAC(self):

        if db.tbDevice(mMAC=request.vars.mMAC)==None:
            return False
        else:
            return True

    #Check if device exists.
    def isDeviceAcceptableById(self):

        if db.tbDevice(id=request.vars.mDeviceId)==None:
            return False
        else:
            return True




class MyForms:

	def __init__(self):
		pass


	'''
		This method correct the error generated
		by user when it writes something with quotes....
	'''

	def correctStringFields(self, mForm, mVars = ['mName']):
		for mVar in mVars:
			mForm.vars[mVar] = mForm.vars[mVar].replace('"', "'")
		pass



class Utilities:

	def __init__(self):
		pass



	#Get date to make a query in the future.
	def getDate(self, mYearIndex=1, mMonthIndex=2, mDayIndex=3 ):

	    mDay   = request.now.day
	    mYear  = request.now.year
	    mMonth = request.now.month

	    try:
	        if(len(request.args) >= 4):
		        #Check if the year is valid.
		        if request.args[mYearIndex]>0:
		            #Check if the month is correct.
		            if (int(request.args[mMonthIndex]) > 0) and (int(request.args[mMonthIndex]) < 13) :
		                #Check if the day is correct.
		                if (int(request.args[mDayIndex]) > 0) and (int(request.args[mDayIndex]) < 32) :
		                    return request.args[mYearIndex], request.args[mMonthIndex], request.args[mDayIndex]

	    except Exception as mError:
	        print "getDate", mError

	    return mYear, mMonth, mDay



	#Get a beautiful datetime.
	@staticmethod
	def adjustDateTime(mValue=request.now):

		return mValue.strftime("%d/%m/%Y - %Hh %Mm")


	#Get month name by a number.
	def getMonthName(self, mMonth):

		    mMonth = int(mMonth)
		    if mMonth == 1:
		        return T('January')
		    if mMonth == 2:
		        return T('February')
		    if mMonth == 3:
		        return T('March')
		    if mMonth == 4:
		        return T('April')
		    if mMonth == 5:
		        return T('May')
		    if mMonth == 6:
		        return T('June')
		    if mMonth == 7:
		        return T('July')
		    if mMonth == 8:
		        return T('August')
		    if mMonth == 9:
		        return T('September')
		    if mMonth == 10:
		        return T('October')
		    if mMonth == 11:
		        return T('November')
		    if mMonth == 12:
		        return T('December')

		    return T("No valid month.")



class Convert:

		@staticmethod
		def toString(mData):
			try:
				return mData.encode('utf-8')
			except:
				return str(mData)


		@staticmethod
		def dateTimeToInt(mData):
			try:
				return int( str(mData).replace(" ", "").replace("/", "").replace("-", "").replace(":", "") )
			except:
				return 0



		@staticmethod
		def intToDateTime(mData):
			from datetime import datetime
			try:
				mTemp = str( mData )
				mResult = mTemp[0:4] + '-' + mTemp[4:6] + '-' + mTemp[6:8] + ' '
				mResult += mTemp[8:10] + ':' + mTemp[10:12] + ':' + mTemp[12:14]

				return datetime.strptime(mResult, "%Y-%m-%d %H:%M:%S")
			except mError as Exception:
				print mError
				return request.now


class Validator:

	@staticmethod
	def is_integer( mString):

		try:
			mNumber = int(mString)
			return True
		except Exception as mError:
			print "is_integer", mError
			return False


	@staticmethod
	def has_args( mLength):

		if len(request.args)==mLength:
			return True
		else:
			return False


	@staticmethod
	def has_vars( mLength):

		if len(request.vars)==mLength:
			return True
		else:
			return False


	@staticmethod
	def valide_args( mLength, mUrl = URL('default', 'index')):
		#print mLength
		if not len(request.args)==mLength:
			#print mUrl
			redirect(mUrl)
		pass



	@staticmethod
	def valide_minimum_args( mLength, mUrl = URL('default', 'index')):
		#print mLength
		if not len(request.args)>=mLength:
			#print mUrl
			redirect(mUrl)
		pass



	@staticmethod
	def valide_minimum_vars( mLength, mUrl = URL('default', 'index')):
		#print mLength
		if not len(request.vars)>=mLength:
			#print mUrl
			redirect(mUrl)
		pass


	@staticmethod
	def has_minimum_vars( mLength, mUrl = URL('default', 'index')):

		if not len(request.vars)>=mLength:
			return False

		return True



	@staticmethod
	def form_process( mForm, mUrl = URL('default', 'index'), mSuccessMessage=T('Added successfully!'),
						mErrorMessage=T('Erros in form, please check it out.'), mValidation=None, mOnAccepted=None, mOnErrors=None):

		processed = None

		if mValidation == None:
			processed = mForm.process()
		else:
			processed = mForm.process(onvalidation=mValidation)

		if processed.accepted:
			if not mOnAccepted == None:
				mOnAccepted(mForm)
			MessageBox(T(mSuccessMessage)).showSuccess()
			redirect(mUrl)
		elif mForm.errors:
			if not mOnErrors == None:
				mOnErrors(mForm)
			MessageBox(T(mErrorMessage)).showError()

		pass




	@staticmethod
	def check_is_group_owner( mId, mTable, mUrl=URL('default', 'index')):

		try:
			mGroup = db.auth_group(id=db(auth.user_id == db.auth_membership.user_id).select()[0].group_id)
			mItem = mTable(mId)

			if mGroup == None:
				redirect(mUrl)

			if not mGroup.id == mItem.mUserGroup:
				redirect(mUrl)

		except mError:
			print 'check_is_group_owner except', mError
			print  mId, mTable, mUrl
			redirect(mUrl)




	@staticmethod
	def get_date():

		mYear = request.now.year
		mMonth = request.now.month

		try:
			int(mYear)
			if has_args(2):
				if (int(request.args[1]) > 0) and (int(request.args[1]) < 13) :
					return request.args[0], request.args[1]

			return mYear, mMonth
		except Exception as mError:
			print mError
			return mYear, mMonth

	pass


class SQL:

	def __init__(self):
		self.mInjetionWords=['select', 'update', 'delete', 'drop', 'table']
		pass

	def check_string_in_list(self, mField, mWords):
		mResult = False
		for mWord in mWords:
			if mWord in mField:
				return True

		return mResult


	def has_injection(self, mFields):
		mResult = False
		for mField in mFields:
			if self.check_string_in_list(mField.lower(), self.mInjetionWords):
				return True

		return mResult



import json
class Json:

	@staticmethod
	def SuccessResult():
		return json.dumps([{'mResult':'true'}])


	@staticmethod
	def FailResult():
		return json.dumps([{'mResult':'false'}])

	@staticmethod
	def NullResult():
		return json.dumps([{"mResult":"NULL"}])


class MyPDF:

	@staticmethod
	def getConst():
		return 'pdf'

	@staticmethod
	def isRequestingExport():
		if request.vars.mExport == MyPDF.getConst():
			return True
		else:
			return False


	def __init__(self, mHtmlFile, mPageData):

		self.mPageData = mPageData
		self.mHtmlFile = mHtmlFile
		pass

	def generate(self):
		try:
			mHtml = response.render(self.mHtmlFile, self.mPageData)
			return plugin_appreport.REPORTPISA(html = mHtml)
		except Exception as mError:
			print mError
			return 'Error pdf export: '+ str(mError)


class MyFile:

	def __init__(self, mPath):
		self.mPath = mPath
		self.mFile = None
		pass

	def openWrite(self):
		self.mFile = open(self.mPath, 'w')
		pass

	def openRead(self):
		self.mFile = open(self.mPath, 'r')
		pass

	def write(self, mData):
		self.mFile.write(mData)

	def writeLine(self, mData):
		self.mFile.write(mData+'\n')

	def read(self):
		return self.mFile

	def close(self):
		if not self.mFile == None:
			self.mFile.close()

	@staticmethod
	def exists(mFile):
		import os.path, os
		if ( (not os.path.isfile(mFile) ) or (os.stat(mFile).st_size ==0) ):
			return False
		else:
			return True
