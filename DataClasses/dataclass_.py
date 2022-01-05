from dataclasses import dataclass, field
  
@dataclass
class order:
    orderID: int
    customerID: int
    salespersonPersonID: int
    pickedByPersonID: int
    contactPersonID: int
    backorderOrderID: int
    expectedDeliveryDate: str
    orderDate: str
    customerPurchaseOrderNumber: int
    isUndersupplyBackOrdered: int
    comments: str
    deliveryinstructions: str
    internalComments: str
    pickingCompletedWhen: str
    lastEditedBy: str
    lastEditedWhen: str

    def __gt__(self,other):
        return self.orderDate > other.orderDate
    
    def __ge__(self,other):
        return self.orderDate >= other.orderDate

@dataclass
class invoices:
    invoiceID: int
    customerID: int
    billtoCustomerID: int
    orderID: int
    deliveryMethodID: int
    contactPersonID: int
    accountsPersonID: int
    salespersonPersonID: int
    customerPurcahseOrderNumber: int
    invoiceDate = str
    isCreditNote: int #bool
    creditNoteReason: str
    comments: str
    deliveryInstructions: str
    internalComments: str
    totalDryItems: int
    totalChillerItems: int
    deliveryRun: str
    runPosition: str
    returnedDeliveryData: str
    confirmedDeliveryTime: str
    confirmedReceivedBy: str
    lastEditedBy: str
    lastEditedWhen: str

    def __gt__(self,other):
        return self.invoiceDate > other.invoiceDate
    
    def __ge__(self,other):
        return self.invoiceDate >= other.invoiceDate

@dataclass
class customer:
    customerID: int
    customerName: str
    billtoCustomeriD: int
    customerCategoryID: int
    buyingGroupID: int
    primaryContactPersonID: int
    alternateContactPersonID: int
    deliveryMethodID: int
    deliveryCityID: int
    postalCityID: int
    creditLimit: int
    accountOpenedDate: str
    standardDiscountPercentage: int
    isStatementSend: int #bool
    isonCreditHold: int #bool
    paymentDays: int
    phoneNumber: str
    faxNumber: str
    deliveryRun: str
    runPosition: str
    websiteURL: str
    deliveryAddressLine1: str
    deliveryAddressLine2: str
    deliveryPostalCode: str
    deliveryLocation: str
    postalAddressLine1: str
    postalAddressLine2: str
    postalPostalCode: str
    lastEditedBy: str
    validFrom: str
    validTo: str
