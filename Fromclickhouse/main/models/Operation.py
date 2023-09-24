from __future__ import division, print_function, absolute_import


class Operation:

    #Project id
    _projectId = None

    @property
    def projectId(self):
        return self._projectId
    
    @projectId.setter
    def projectId(self, value):
        self._projectId = value

    # Revenue name
    _revenueName = None

    @property
    def revenueName(self):
        return self._revenueName

    @revenueName.setter
    def revenueName(self, value):
        self._revenueName = value

    # Proposal_id
    _proposalId = None

    @property
    def proposalId(self):
        return self._proposalId

    @proposalId.setter
    def proposalId(self, value):
        self._proposalId = value

    # Generation task id
    _generationTaskId = None

    @property
    def generationTaskId(self):
        return self._generationTaskId

    @generationTaskId.setter
    def generationTaskId(self, value):
        self._generationTaskId = value

    # Task id
    _taskId = None

    @property
    def taskId(self):
        return self._taskId

    @taskId.setter
    def taskId(self, value):
        self._taskId = value

    # Business id
    _businessId = None

    @property
    def businessId(self):
        return self._businessId

    @businessId.setter
    def businessId(self, value):
        self._businessId = value

    # Begin Time
    _beginTime = None

    @property
    def beginTime(self):
        return self._beginTime

    @beginTime.setter
    def beginTime(self, value):
        self._beginTime = value

    # End Time
    _endTime = None

    @property
    def endTime(self):
        return self._endTime

    @endTime.setter
    def endTime(self, value):
        self._endTime = value

    # costperunit
    _costPerUnit = 0.2

    @property
    def costPerUnit(self):
        return self._costPerUnit
    
    @costPerUnit.setter
    def costPerUnit(self, value):
        self._costPerUnit = value


    # Battery_capacity
    _batteryCapacity = None

    @property
    def batteryCapacity(self):
        return self._batteryCapacity

    @batteryCapacity.setter
    def batteryCapacity(self, value):
        self._batteryCapacity = value

    # Inflation
    _inflation = 0

    @property
    def inflation(self):
        return self._inflation

    @inflation.setter
    def inflation(self, value):
        self._inflation = value

    #maxChargeDischarge
    _maxChargeDischarge = 0.01

    @property
    def maxChargeDischarge(self):
        return self._maxChargeDischarge
    
    @maxChargeDischarge.setter
    def maxChargeDischarge(self, value):
        self._maxChargeDischarge = value

    # Connection_point_limitation
    _connectionPointLimitation = float('inf')

    @property
    def connectionPointLimitation(self):
        return self._connectionPointLimitation

    @connectionPointLimitation.setter
    def connectionPointLimitation(self, value):
        self._connectionPointLimitation = value

    # Time interval
    _interval = None

    @property
    def interval(self):
        return self._interval

    @interval.setter
    def interval(self, value):
        self._interval = value

    # Operation type
    _operationType = None

    @property
    def operationType(self):
        return self._operationType

    @operationType.setter
    def operationType(self, value):
        self._operationType = value

    # Price matrix
    _priceMatrix = None

    @property
    def priceMatrix(self):
        return self._priceMatrix

    @priceMatrix.setter
    def priceMatrix(self, value):
        self._priceMatrix = value

    # Price matrix_data
    _priceMatrixData = None

    @property
    def priceMatrixData(self):
        return self._priceMatrixData

    @priceMatrixData.setter
    def priceMatrixData(self, value):
        self._priceMatrixData = value


    # Minimum soc
    _minSOC = 0

    @property
    def minSOC(self):
        return self._minSOC

    @minSOC.setter
    def minSOC(self, value):
        self._minSOC = value

    #rte
    _rte =0.01

    @property
    def rte(self):
        return self._rte
    
    @rte.setter
    def rte(self,value):
        self._rte = value

    #strategy
    _strategy = 1

    @property
    def strategy(self):
        return self._strategy
    
    @strategy.setter
    def strategy(self, value):
        self._strategy = value

    # Maximum soc
    _maxSOC = 100

    @property
    def maxSOC(self):
        return self._maxSOC

    @maxSOC.setter
    def maxSOC(self, value):
        self._maxSOC = value

    # unitChargeDischarge
    _unitChargeDischarge = 0.01

    @property
    def unitChargeDischarge(self):
        return self._unitChargeDischarge
    
    @unitChargeDischarge.setter
    def unitChargeDischarge(self, value):
        self._unitChargeDischarge = value

    #country
    _country = None

    @property
    def country(self):
        return self._country
    
    @country.setter
    def country(self,value):
        self._country = value


    # state
    _state = None
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, value):
        self._state = value

    # market
    _market = None
    @property
    def market(self):
        return self._market
    
    @market.setter
    def market(self,value):
        self._market = value

    # year
    _year = None
    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self,value):
        self._year = value


