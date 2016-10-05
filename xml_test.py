import xmltodict, json

addOrder = """<?xml version="1.0" encoding="utf-8"?>
<GetOrderTransactionsResponse xmlns="urn:ebay:apis:eBLBaseComponents">
  <!-- Call-specific Output Fields -->
  <OrderArray> OrderArrayType
    <Order> OrderType
      <AdjustmentAmount currencyID="CurrencyCodeType"> AmountType (double) </AdjustmentAmount>
      <AmountPaid currencyID="CurrencyCodeType"> AmountType (double) </AmountPaid>
      <AmountSaved currencyID="CurrencyCodeType"> AmountType (double) </AmountSaved>
      <BuyerCheckoutMessage> string </BuyerCheckoutMessage>
      <BuyerPackageEnclosures> BuyerPackageEnclosuresType
        <BuyerPackageEnclosure type="PaymentInstructionCodeType"> BuyerPackageEnclosureType (string) </BuyerPackageEnclosure>
        <!-- ... more BuyerPackageEnclosure nodes allowed here ... -->
      </BuyerPackageEnclosures>
      <BuyerTaxIdentifier> TaxIdentifierType
        <Attribute name="TaxIdentifierAttributeCodeType"> TaxIdentifierAttributeType (string) </Attribute>
        <!-- ... more Attribute nodes allowed here ... -->
        <ID> string </ID>
        <Type> ValueTypeCodeType </Type>
      </BuyerTaxIdentifier>
      <!-- ... more BuyerTaxIdentifier nodes allowed here ... -->
      <BuyerUserID> UserIDType (string) </BuyerUserID>
      <CancelDetail> CancelDetailType
        <CancelCompleteDate> dateTime </CancelCompleteDate>
        <CancelIntiationDate> dateTime </CancelIntiationDate>
        <CancelIntiator> token </CancelIntiator>
        <CancelReason> token </CancelReason>
        <CancelReasonDetails> string </CancelReasonDetails>
      </CancelDetail>
      <!-- ... more CancelDetail nodes allowed here ... -->
      <CancelReason> token </CancelReason>
      <CancelReasonDetails> string </CancelReasonDetails>
      <CancelStatus> CancelStatusCodeType </CancelStatus>
      <CheckoutStatus> CheckoutStatusType
        <eBayPaymentStatus> PaymentStatusCodeType </eBayPaymentStatus>
        <IntegratedMerchantCreditCardEnabled> boolean </IntegratedMerchantCreditCardEnabled>
        <LastModifiedTime> dateTime </LastModifiedTime>
        <PaymentInstrument> BuyerPaymentInstrumentCodeType </PaymentInstrument>
        <PaymentMethod> BuyerPaymentMethodCodeType </PaymentMethod>
        <Status> CompleteStatusCodeType </Status>
      </CheckoutStatus>
      <ContainseBayPlusTransaction> boolean </ContainseBayPlusTransaction>
      <CreatedTime> dateTime </CreatedTime>
      <CreatingUserRole> TradingRoleCodeType </CreatingUserRole>
      <ExtendedOrderID> string </ExtendedOrderID>
      <ExternalTransaction> ExternalTransactionType
        <ExternalTransactionStatus> PaymentTransactionStatusCodeType </ExternalTransactionStatus>
        <ExternalTransactionTime> dateTime </ExternalTransactionTime>
        <FeeOrCreditAmount currencyID="CurrencyCodeType"> AmountType (double) </FeeOrCreditAmount>
        <PaymentOrRefundAmount currencyID="CurrencyCodeType"> AmountType (double) </PaymentOrRefundAmount>
      </ExternalTransaction>
      <!-- ... more ExternalTransaction nodes allowed here ... -->
      <IntegratedMerchantCreditCardEnabled> boolean </IntegratedMerchantCreditCardEnabled>
      <IsMultiLegShipping> boolean </IsMultiLegShipping>
      <LogisticsPlanType> token </LogisticsPlanType>
      <MonetaryDetails> PaymentsInformationType
        <Payments> PaymentInformationType
          <Payment> PaymentTransactionType
            <FeeOrCreditAmount currencyID="CurrencyCodeType"> AmountType (double) </FeeOrCreditAmount>
            <Payee type="UserIdentityCodeType"> UserIdentityType (string) </Payee>
            <Payer type="UserIdentityCodeType"> UserIdentityType (string) </Payer>
            <PaymentAmount currencyID="CurrencyCodeType"> AmountType (double) </PaymentAmount>
            <PaymentReferenceID type="TransactionReferenceCodeType"> TransactionReferenceType (string) </PaymentReferenceID>
            <!-- ... more PaymentReferenceID nodes allowed here ... -->
            <PaymentStatus> PaymentTransactionStatusCodeType </PaymentStatus>
            <PaymentTime> dateTime </PaymentTime>
            <ReferenceID type="TransactionReferenceCodeType"> TransactionReferenceType (string) </ReferenceID>
          </Payment>
          <!-- ... more Payment nodes allowed here ... -->
        </Payments>
        <Refunds> RefundInformationType
          <Refund> RefundTransactionInfoType
            <FeeOrCreditAmount currencyID="CurrencyCodeType"> AmountType (double) </FeeOrCreditAmount>
            <ReferenceID type="TransactionReferenceCodeType"> TransactionReferenceType (string) </ReferenceID>
            <RefundAmount currencyID="CurrencyCodeType"> AmountType (double) </RefundAmount>
            <RefundStatus> PaymentTransactionStatusCodeType </RefundStatus>
            <RefundTime> dateTime </RefundTime>
            <RefundTo type="UserIdentityCodeType"> UserIdentityType (string) </RefundTo>
            <RefundType> RefundSourceTypeCodeType </RefundType>
          </Refund>
          <!-- ... more Refund nodes allowed here ... -->
        </Refunds>
      </MonetaryDetails>
      <MultiLegShippingDetails> MultiLegShippingDetailsType
        <SellerShipmentToLogisticsProvider> MultiLegShipmentType
          <ShippingServiceDetails> MultiLegShippingServiceType
            <ShippingService> token </ShippingService>
            <TotalShippingCost currencyID="CurrencyCodeType"> AmountType (double) </TotalShippingCost>
          </ShippingServiceDetails>
          <ShippingTimeMax> int </ShippingTimeMax>
          <ShippingTimeMin> int </ShippingTimeMin>
          <ShipToAddress> AddressType
            <AddressAttribute type="AddressAttributeCodeType"> AddressAttributeType (string) </AddressAttribute>
            <!-- ... more AddressAttribute nodes allowed here ... -->
            <AddressID> string </AddressID>
            <AddressOwner> AddressOwnerCodeType </AddressOwner>
            <AddressUsage> AddressUsageCodeType </AddressUsage>
            <CityName> string </CityName>
            <Country> CountryCodeType </Country>
            <CountryName> string </CountryName>
            <ExternalAddressID> string </ExternalAddressID>
            <Name> string </Name>
            <Phone> string </Phone>
            <PostalCode> string </PostalCode>
            <ReferenceID> string </ReferenceID>
            <StateOrProvince> string </StateOrProvince>
            <Street1> string </Street1>
            <Street2> string </Street2>
          </ShipToAddress>
        </SellerShipmentToLogisticsProvider>
      </MultiLegShippingDetails>
      <OrderID> OrderIDType (string) </OrderID>
      <OrderStatus> OrderStatusCodeType </OrderStatus>
      <PaidTime> dateTime </PaidTime>
      <PaymentHoldDetails> PaymentHoldDetailType
        <ExpectedReleaseDate> dateTime </ExpectedReleaseDate>
        <NumOfReqSellerActions> int </NumOfReqSellerActions>
        <PaymentHoldReason> PaymentHoldReasonCodeType </PaymentHoldReason>
        <RequiredSellerActionArray> RequiredSellerActionArrayType
          <RequiredSellerAction> RequiredSellerActionCodeType </RequiredSellerAction>
          <!-- ... more RequiredSellerAction values allowed here ... -->
        </RequiredSellerActionArray>
      </PaymentHoldDetails>
      <PaymentHoldStatus> PaymentHoldStatusCodeType </PaymentHoldStatus>
      <PaymentMethods> BuyerPaymentMethodCodeType </PaymentMethods>
      <!-- ... more PaymentMethods values allowed here ... -->
      <PickupDetails> PickupDetailsType
        <PickupOptions> PickupOptionsType
          <PickupMethod> token </PickupMethod>
          <PickupPriority> int </PickupPriority>
        </PickupOptions>
        <!-- ... more PickupOptions nodes allowed here ... -->
      </PickupDetails>
      <PickupMethodSelected> PickupMethodSelectedType
        <MerchantPickupCode> string </MerchantPickupCode>
        <PickupFulfillmentTime> dateTime </PickupFulfillmentTime>
        <PickupLocationUUID> string </PickupLocationUUID>
        <PickupMethod> token </PickupMethod>
        <PickupStatus> PickupStatusCodeType </PickupStatus>
        <PickupStoreID> string </PickupStoreID>
      </PickupMethodSelected>
      <RefundArray> RefundArrayType
        <Refund> RefundType
          <RefundAmount currencyID="CurrencyCodeType"> AmountType (double) </RefundAmount>
          <RefundID> string </RefundID>
        </Refund>
        <!-- ... more Refund nodes allowed here ... -->
      </RefundArray>
      <SellerEmail> string </SellerEmail>
      <SellerUserID> UserIDType (string) </SellerUserID>
      <ShippedTime> dateTime </ShippedTime>
      <ShippingAddress> AddressType
        <AddressAttribute type="AddressAttributeCodeType"> AddressAttributeType (string) </AddressAttribute>
        <!-- ... more AddressAttribute nodes allowed here ... -->
        <AddressID> string </AddressID>
        <AddressOwner> AddressOwnerCodeType </AddressOwner>
        <AddressUsage> AddressUsageCodeType </AddressUsage>
        <CityName> string </CityName>
        <Country> CountryCodeType </Country>
        <CountryName> string </CountryName>
        <ExternalAddressID> string </ExternalAddressID>
        <Name> string </Name>
        <Phone> string </Phone>
        <PostalCode> string </PostalCode>
        <StateOrProvince> string </StateOrProvince>
        <Street1> string </Street1>
        <Street2> string </Street2>
      </ShippingAddress>
      <ShippingConvenienceCharge currencyID="CurrencyCodeType"> AmountType (double) </ShippingConvenienceCharge>
      <ShippingDetails> ShippingDetailsType
        <ChangePaymentInstructions> boolean </ChangePaymentInstructions>
        <CODCost currencyID="CurrencyCodeType"> AmountType (double) </CODCost>
        <ExcludeShipToLocation> string </ExcludeShipToLocation>
        <!-- ... more ExcludeShipToLocation values allowed here ... -->
        <InsuranceFee currencyID="CurrencyCodeType"> AmountType (double) </InsuranceFee>
        <InsuranceOption> InsuranceOptionCodeType </InsuranceOption>
        <InsuranceWanted> boolean </InsuranceWanted>
        <InternationalShippingServiceOption> InternationalShippingServiceOptionsType
          <ImportCharge currencyID="CurrencyCodeType"> AmountType (double) </ImportCharge>
          <ShippingInsuranceCost currencyID="CurrencyCodeType"> AmountType (double) </ShippingInsuranceCost>
          <ShippingService> token </ShippingService>
          <ShippingServiceAdditionalCost currencyID="CurrencyCodeType"> AmountType (double) </ShippingServiceAdditionalCost>
          <ShippingServiceCost currencyID="CurrencyCodeType"> AmountType (double) </ShippingServiceCost>
          <ShippingServicePriority> int </ShippingServicePriority>
          <ShipToLocation> string </ShipToLocation>
          <!-- ... more ShipToLocation values allowed here ... -->
        </InternationalShippingServiceOption>
        <!-- ... more InternationalShippingServiceOption nodes allowed here ... -->
        <SalesTax> SalesTaxType
          <SalesTaxAmount currencyID="CurrencyCodeType"> AmountType (double) </SalesTaxAmount>
          <SalesTaxPercent> float </SalesTaxPercent>
          <SalesTaxState> string </SalesTaxState>
          <ShippingIncludedInTax> boolean </ShippingIncludedInTax>
        </SalesTax>
        <SellingManagerSalesRecordNumber> int </SellingManagerSalesRecordNumber>
        <ShipmentTrackingDetails> ShipmentTrackingDetailsType
          <ShipmentTrackingNumber> string </ShipmentTrackingNumber>
          <ShippingCarrierUsed> string </ShippingCarrierUsed>
        </ShipmentTrackingDetails>
        <!-- ... more ShipmentTrackingDetails nodes allowed here ... -->
        <ShippingServiceOptions> ShippingServiceOptionsType
          <ExpeditedService> boolean </ExpeditedService>
          <ImportCharge currencyID="CurrencyCodeType"> AmountType (double) </ImportCharge>
          <LogisticPlanType> string </LogisticPlanType>
          <ShippingInsuranceCost currencyID="CurrencyCodeType"> AmountType (double) </ShippingInsuranceCost>
          <ShippingPackageInfo> ShippingPackageInfoType
            <ActualDeliveryTime> dateTime </ActualDeliveryTime>
            <ScheduledDeliveryTimeMax> dateTime </ScheduledDeliveryTimeMax>
            <ScheduledDeliveryTimeMin> dateTime </ScheduledDeliveryTimeMin>
            <ShippingTrackingEvent> token </ShippingTrackingEvent>
            <StoreID> string </StoreID>
          </ShippingPackageInfo>
          <!-- ... more ShippingPackageInfo nodes allowed here ... -->
          <ShippingService> token </ShippingService>
          <ShippingServiceAdditionalCost currencyID="CurrencyCodeType"> AmountType (double) </ShippingServiceAdditionalCost>
          <ShippingServiceCost currencyID="CurrencyCodeType"> AmountType (double) </ShippingServiceCost>
          <ShippingServicePriority> int </ShippingServicePriority>
          <ShippingSurcharge currencyID="CurrencyCodeType"> AmountType (double) </ShippingSurcharge>
        </ShippingServiceOptions>
        <!-- ... more ShippingServiceOptions nodes allowed here ... -->
        <TaxTable> TaxTableType
          <TaxJurisdiction> TaxJurisdictionType
            <JurisdictionID> string </JurisdictionID>
            <SalesTaxPercent> float </SalesTaxPercent>
            <ShippingIncludedInTax> boolean </ShippingIncludedInTax>
          </TaxJurisdiction>
          <!-- ... more TaxJurisdiction nodes allowed here ... -->
        </TaxTable>
      </ShippingDetails>
      <ShippingServiceSelected> ShippingServiceOptionsType
        <ExpeditedService> boolean </ExpeditedService>
        <ImportCharge currencyID="CurrencyCodeType"> AmountType (double) </ImportCharge>
        <LogisticPlanType> string </LogisticPlanType>
        <ShippingInsuranceCost currencyID="CurrencyCodeType"> AmountType (double) </ShippingInsuranceCost>
        <ShippingPackageInfo> ShippingPackageInfoType
          <ActualDeliveryTime> dateTime </ActualDeliveryTime>
          <EstimatedDeliveryTimeMax> dateTime </EstimatedDeliveryTimeMax>
          <EstimatedDeliveryTimeMin> dateTime </EstimatedDeliveryTimeMin>
          <ScheduledDeliveryTimeMax> dateTime </ScheduledDeliveryTimeMax>
          <ScheduledDeliveryTimeMin> dateTime </ScheduledDeliveryTimeMin>
          <ShippingTrackingEvent> token </ShippingTrackingEvent>
          <StoreID> string </StoreID>
        </ShippingPackageInfo>
        <!-- ... more ShippingPackageInfo nodes allowed here ... -->
        <ShippingService> token </ShippingService>
        <ShippingServiceAdditionalCost currencyID="CurrencyCodeType"> AmountType (double) </ShippingServiceAdditionalCost>
        <ShippingServiceCost currencyID="CurrencyCodeType"> AmountType (double) </ShippingServiceCost>
        <ShippingServicePriority> int </ShippingServicePriority>
        <ShippingSurcharge currencyID="CurrencyCodeType"> AmountType (double) </ShippingSurcharge>
      </ShippingServiceSelected>
      <Subtotal currencyID="CurrencyCodeType"> AmountType (double) </Subtotal>
      <Total currencyID="CurrencyCodeType"> AmountType (double) </Total>
      <TransactionArray> TransactionArrayType
        <Transaction> TransactionType
          <ActualHandlingCost currencyID="CurrencyCodeType"> AmountType (double) </ActualHandlingCost>
          <ActualShippingCost currencyID="CurrencyCodeType"> AmountType (double) </ActualShippingCost>
          <AdjustmentAmount currencyID="CurrencyCodeType"> AmountType (double) </AdjustmentAmount>
          <AmountPaid currencyID="CurrencyCodeType"> AmountType (double) </AmountPaid>
          <BestOfferSale> boolean </BestOfferSale>
          <Buyer> UserType
            <AboutMePage> boolean </AboutMePage>
            <eBayGoodStanding> boolean </eBayGoodStanding>
            <EIASToken> string </EIASToken>
            <Email> string </Email>
            <FeedbackPrivate> boolean </FeedbackPrivate>
            <FeedbackRatingStar> FeedbackRatingStarCodeType </FeedbackRatingStar>
            <FeedbackScore> int </FeedbackScore>
            <IDVerified> boolean </IDVerified>
            <NewUser> boolean </NewUser>
            <RegistrationDate> dateTime </RegistrationDate>
            <Site> SiteCodeType </Site>
            <StaticAlias> string </StaticAlias>
            <Status> UserStatusCodeType </Status>
            <UserAnonymized> boolean </UserAnonymized>
            <UserFirstName> string </UserFirstName>
            <UserID> UserIDType (string) </UserID>
            <UserIDChanged> boolean </UserIDChanged>
            <UserIDLastChanged> dateTime </UserIDLastChanged>
            <UserLastName> string </UserLastName>
            <VATStatus> VATStatusCodeType </VATStatus>
          </Buyer>
          <BuyerGuaranteePrice currencyID="CurrencyCodeType"> AmountType (double) </BuyerGuaranteePrice>
          <BuyerPackageEnclosures> BuyerPackageEnclosuresType
            <BuyerPackageEnclosure type="PaymentInstructionCodeType"> BuyerPackageEnclosureType (string) </BuyerPackageEnclosure>
            <!-- ... more BuyerPackageEnclosure nodes allowed here ... -->
          </BuyerPackageEnclosures>
          <CartID> string </CartID>
          <ConvertedAdjustmentAmount currencyID="CurrencyCodeType"> AmountType (double) </ConvertedAdjustmentAmount>
          <ConvertedAmountPaid currencyID="CurrencyCodeType"> AmountType (double) </ConvertedAmountPaid>
          <ConvertedTransactionPrice currencyID="CurrencyCodeType"> AmountType (double) </ConvertedTransactionPrice>
          <CreatedDate> dateTime </CreatedDate>
          <DepositType> DepositTypeCodeType </DepositType>
          <DigitalDeliverySelected> DigitalDeliverySelectedType
            <DeliveryDetails> DeliveryDetailsType
              <Recipient> DigitalDeliveryUserType
                <Email> string </Email>
                <Name> string </Name>
              </Recipient>
              <Sender> DigitalDeliveryUserType
                <Email> string </Email>
                <Name> string </Name>
              </Sender>
            </DeliveryDetails>
            <DeliveryMethod> token </DeliveryMethod>
            <DeliveryStatus> DeliveryStatusType
              <Email> token </Email>
            </DeliveryStatus>
          </DigitalDeliverySelected>
          <eBayPlusTransaction> boolean </eBayPlusTransaction>
          <ExtendedOrderID> string </ExtendedOrderID>
          <ExternalTransaction> ExternalTransactionType
            <ExternalTransactionStatus> PaymentTransactionStatusCodeType </ExternalTransactionStatus>
            <ExternalTransactionTime> dateTime </ExternalTransactionTime>
            <FeeOrCreditAmount currencyID="CurrencyCodeType"> AmountType (double) </FeeOrCreditAmount>
            <PaymentOrRefundAmount currencyID="CurrencyCodeType"> AmountType (double) </PaymentOrRefundAmount>
          </ExternalTransaction>
          <!-- ... more ExternalTransaction nodes allowed here ... -->
          <FinalValueFee currencyID="CurrencyCodeType"> AmountType (double) </FinalValueFee>
          <Gift> boolean </Gift>
          <GiftSummary> GiftSummaryType
            <Message> string </Message>
          </GiftSummary>
          <IntangibleItem> boolean </IntangibleItem>
          <InventoryReservationID> string </InventoryReservationID>
          <InvoiceSentTime> dateTime </InvoiceSentTime>
          <IsMultiLegShipping> boolean </IsMultiLegShipping>
          <Item> ItemType
            <ApplicationData> string </ApplicationData>
            <AutoPay> boolean </AutoPay>
            <BuyerProtection> BuyerProtectionCodeType </BuyerProtection>
            <BuyItNowPrice currencyID="CurrencyCodeType"> AmountType (double) </BuyItNowPrice>
            <Charity> CharityType
              <CharityID> string </CharityID>
              <CharityListing> boolean </CharityListing>
              <CharityName> string </CharityName>
              <CharityNumber> int </CharityNumber>
              <DonationPercent> float </DonationPercent>
            </Charity>
            <IntegratedMerchantCreditCardEnabled> boolean </IntegratedMerchantCreditCardEnabled>
            <ItemID> ItemIDType (string) </ItemID>
            <ListingType> ListingTypeCodeType </ListingType>
            <PrivateListing> boolean </PrivateListing>
            <SellingStatus> SellingStatusType
              <ConvertedCurrentPrice currencyID="CurrencyCodeType"> AmountType (double) </ConvertedCurrentPrice>
              <CurrentPrice currencyID="CurrencyCodeType"> AmountType (double) </CurrentPrice>
              <FinalValueFee currencyID="CurrencyCodeType"> AmountType (double) </FinalValueFee>
              <ListingStatus> ListingStatusCodeType </ListingStatus>
            </SellingStatus>
          </Item>
          <LogisticsPlanType> token </LogisticsPlanType>
          <MonetaryDetails> PaymentsInformationType
            <Payments> PaymentInformationType
              <Payment> PaymentTransactionType
                <FeeOrCreditAmount currencyID="CurrencyCodeType"> AmountType (double) </FeeOrCreditAmount>
                <Payee type="UserIdentityCodeType"> UserIdentityType (string) </Payee>
                <Payer type="UserIdentityCodeType"> UserIdentityType (string) </Payer>
                <PaymentAmount currencyID="CurrencyCodeType"> AmountType (double) </PaymentAmount>
                <PaymentReferenceID type="TransactionReferenceCodeType"> TransactionReferenceType (string) </PaymentReferenceID>
                <!-- ... more PaymentReferenceID nodes allowed here ... -->
                <PaymentStatus> PaymentTransactionStatusCodeType </PaymentStatus>
                <PaymentTime> dateTime </PaymentTime>
                <ReferenceID type="TransactionReferenceCodeType"> TransactionReferenceType (string) </ReferenceID>
              </Payment>
              <!-- ... more Payment nodes allowed here ... -->
            </Payments>
            <Refunds> RefundInformationType
              <Refund> RefundTransactionInfoType
                <FeeOrCreditAmount currencyID="CurrencyCodeType"> AmountType (double) </FeeOrCreditAmount>
                <ReferenceID type="TransactionReferenceCodeType"> TransactionReferenceType (string) </ReferenceID>
                <RefundAmount currencyID="CurrencyCodeType"> AmountType (double) </RefundAmount>
                <RefundStatus> PaymentTransactionStatusCodeType </RefundStatus>
                <RefundTime> dateTime </RefundTime>
                <RefundTo type="UserIdentityCodeType"> UserIdentityType (string) </RefundTo>
                <RefundType> RefundSourceTypeCodeType </RefundType>
              </Refund>
              <!-- ... more Refund nodes allowed here ... -->
            </Refunds>
          </MonetaryDetails>
          <MultiLegShippingDetails> MultiLegShippingDetailsType
            <SellerShipmentToLogisticsProvider> MultiLegShipmentType
              <ShippingServiceDetails> MultiLegShippingServiceType
                <ShippingService> token </ShippingService>
                <TotalShippingCost currencyID="CurrencyCodeType"> AmountType (double) </TotalShippingCost>
              </ShippingServiceDetails>
              <ShippingTimeMax> int </ShippingTimeMax>
              <ShippingTimeMin> int </ShippingTimeMin>
              <ShipToAddress> AddressType
                <AddressAttribute type="AddressAttributeCodeType"> AddressAttributeType (string) </AddressAttribute>
                <!-- ... more AddressAttribute nodes allowed here ... -->
                <AddressID> string </AddressID>
                <AddressOwner> AddressOwnerCodeType </AddressOwner>
                <AddressUsage> AddressUsageCodeType </AddressUsage>
                <CityName> string </CityName>
                <Country> CountryCodeType </Country>
                <CountryName> string </CountryName>
                <ExternalAddressID> string </ExternalAddressID>
                <Name> string </Name>
                <Phone> string </Phone>
                <PostalCode> string </PostalCode>
                <ReferenceID> string </ReferenceID>
                <StateOrProvince> string </StateOrProvince>
                <Street1> string </Street1>
                <Street2> string </Street2>
              </ShipToAddress>
            </SellerShipmentToLogisticsProvider>
          </MultiLegShippingDetails>
          <OrderLineItemID> string </OrderLineItemID>
          <PaidTime> dateTime </PaidTime>
          <PaymentHoldDetails> PaymentHoldDetailType
            <ExpectedReleaseDate> dateTime </ExpectedReleaseDate>
            <NumOfReqSellerActions> int </NumOfReqSellerActions>
            <PaymentHoldReason> PaymentHoldReasonCodeType </PaymentHoldReason>
            <RequiredSellerActionArray> RequiredSellerActionArrayType
              <RequiredSellerAction> RequiredSellerActionCodeType </RequiredSellerAction>
              <!-- ... more RequiredSellerAction values allowed here ... -->
            </RequiredSellerActionArray>
          </PaymentHoldDetails>
          <PayPalEmailAddress> string </PayPalEmailAddress>
          <PickupMethodSelected> PickupMethodSelectedType
            <MerchantPickupCode> string </MerchantPickupCode>
            <PickupFulfillmentTime> dateTime </PickupFulfillmentTime>
            <PickupLocationUUID> string </PickupLocationUUID>
            <PickupMethod> token </PickupMethod>
            <PickupStatus> PickupStatusCodeType </PickupStatus>
            <PickupStoreID> string </PickupStoreID>
          </PickupMethodSelected>
          <Platform> TransactionPlatformCodeType </Platform>
          <QuantityPurchased> int </QuantityPurchased>
          <RefundArray> RefundArrayType
            <Refund> RefundType
              <RefundAmount currencyID="CurrencyCodeType"> AmountType (double) </RefundAmount>
              <RefundID> string </RefundID>
            </Refund>
            <!-- ... more Refund nodes allowed here ... -->
          </RefundArray>
          <SellerContactBuyerByEmail> boolean </SellerContactBuyerByEmail>
          <SellerDiscounts> SellerDiscountsType
            <OriginalItemPrice currencyID="CurrencyCodeType"> AmountType (double) </OriginalItemPrice>
            <OriginalItemShippingCost currencyID="CurrencyCodeType"> AmountType (double) </OriginalItemShippingCost>
            <OriginalShippingService> token </OriginalShippingService>
            <SellerDiscount> SellerDiscountType
              <CampaignDisplayName> string </CampaignDisplayName>
              <CampaignID> long </CampaignID>
              <ItemDiscountAmount currencyID="CurrencyCodeType"> AmountType (double) </ItemDiscountAmount>
              <ShippingDiscountAmount currencyID="CurrencyCodeType"> AmountType (double) </ShippingDiscountAmount>
            </SellerDiscount>
            <!-- ... more SellerDiscount nodes allowed here ... -->
          </SellerDiscounts>
          <ShippingConvenienceCharge currencyID="CurrencyCodeType"> AmountType (double) </ShippingConvenienceCharge>
          <ShippingServiceSelected> ShippingServiceOptionsType
            <ExpeditedService> boolean </ExpeditedService>
            <ImportCharge currencyID="CurrencyCodeType"> AmountType (double) </ImportCharge>
            <LogisticPlanType> string </LogisticPlanType>
            <ShippingInsuranceCost currencyID="CurrencyCodeType"> AmountType (double) </ShippingInsuranceCost>
            <ShippingPackageInfo> ShippingPackageInfoType
              <ActualDeliveryTime> dateTime </ActualDeliveryTime>
              <EstimatedDeliveryTimeMax> dateTime </EstimatedDeliveryTimeMax>
              <EstimatedDeliveryTimeMin> dateTime </EstimatedDeliveryTimeMin>
              <ScheduledDeliveryTimeMax> dateTime </ScheduledDeliveryTimeMax>
              <ScheduledDeliveryTimeMin> dateTime </ScheduledDeliveryTimeMin>
              <ShippingTrackingEvent> token </ShippingTrackingEvent>
              <StoreID> string </StoreID>
            </ShippingPackageInfo>
            <!-- ... more ShippingPackageInfo nodes allowed here ... -->
            <ShippingService> token </ShippingService>
            <ShippingServiceAdditionalCost currencyID="CurrencyCodeType"> AmountType (double) </ShippingServiceAdditionalCost>
            <ShippingServiceCost currencyID="CurrencyCodeType"> AmountType (double) </ShippingServiceCost>
            <ShippingServicePriority> int </ShippingServicePriority>
            <ShippingSurcharge currencyID="CurrencyCodeType"> AmountType (double) </ShippingSurcharge>
          </ShippingServiceSelected>
          <Status> TransactionStatusType
            <BuyerSelectedShipping> boolean </BuyerSelectedShipping>
            <CheckoutStatus> CheckoutStatusCodeType </CheckoutStatus>
            <CompleteStatus> CompleteStatusCodeType </CompleteStatus>
            <DigitalStatus> DigitalStatusCodeType </DigitalStatus>
            <eBayPaymentStatus> PaymentStatusCodeType </eBayPaymentStatus>
            <InquiryStatus> InquiryStatusCodeType </InquiryStatus>
            <IntegratedMerchantCreditCardEnabled> boolean </IntegratedMerchantCreditCardEnabled>
            <LastTimeModified> dateTime </LastTimeModified>
            <PaymentHoldStatus> PaymentHoldStatusCodeType </PaymentHoldStatus>
            <PaymentInstrument> BuyerPaymentInstrumentCodeType </PaymentInstrument>
            <PaymentMethodUsed> BuyerPaymentMethodCodeType </PaymentMethodUsed>
            <ReturnStatus> ReturnStatusCodeType </ReturnStatus>
          </Status>
          <Taxes> TaxesType
            <TaxDetails> TaxDetailsType
              <Imposition> TaxTypeCodeType </Imposition>
              <TaxAmount currencyID="CurrencyCodeType"> AmountType (double) </TaxAmount>
              <TaxCode> string </TaxCode>
              <TaxDescription> TaxDescriptionCodeType </TaxDescription>
              <TaxOnHandlingAmount currencyID="CurrencyCodeType"> AmountType (double) </TaxOnHandlingAmount>
              <TaxOnShippingAmount currencyID="CurrencyCodeType"> AmountType (double) </TaxOnShippingAmount>
              <TaxOnSubtotalAmount currencyID="CurrencyCodeType"> AmountType (double) </TaxOnSubtotalAmount>
            </TaxDetails>
            <!-- ... more TaxDetails nodes allowed here ... -->
            <TotalTaxAmount currencyID="CurrencyCodeType"> AmountType (double) </TotalTaxAmount>
          </Taxes>
          <TransactionID> string </TransactionID>
          <TransactionPrice currencyID="CurrencyCodeType"> AmountType (double) </TransactionPrice>
          <TransactionSiteID> SiteCodeType </TransactionSiteID>
          <UnpaidItem> UnpaidItemType
            <Status> UnpaidItemCaseStatusTypeCodeType </Status>
            <Type> UnpaidItemCaseOpenTypeCodeType </Type>
          </UnpaidItem>
          <Variation> VariationType
            <SKU> SKUType (string) </SKU>
            <VariationSpecifics> NameValueListArrayType
              <NameValueList> NameValueListType
                <Name> string </Name>
                <Value> string </Value>
                <!-- ... more Value values allowed here ... -->
              </NameValueList>
              <!-- ... more NameValueList nodes allowed here ... -->
            </VariationSpecifics>
            <!-- ... more VariationSpecifics nodes allowed here ... -->
            <VariationTitle> string </VariationTitle>
            <VariationViewItemURL> anyURI </VariationViewItemURL>
          </Variation>
        </Transaction>
        <!-- ... more Transaction nodes allowed here ... -->
      </TransactionArray>
    </Order>
    <!-- ... more Order nodes allowed here ... -->
  </OrderArray>
</GetOrderTransactionsResponse>"""

getItem = """<?xml version="1.0" encoding="UTF-8"?>
<GetItemResponse 
  xmlns="urn:ebay:apis:eBLBaseComponents">
  <Timestamp>2016-08-22T08:50:00.326Z</Timestamp>
  <Ack>Success</Ack>
  <Version>979</Version>
  <Build>E979_CORE_API_18061413_R1</Build>
  <Item>
    <AutoPay>false</AutoPay>
    <BuyerProtection>ItemIneligible</BuyerProtection>
    <BuyItNowPrice currencyID="USD">10.0</BuyItNowPrice>
    <Country>GB</Country>
    <Currency>USD</Currency>
    <GiftIcon>0</GiftIcon>
    <HitCounter>NoHitCounter</HitCounter>
    <ItemID>110182207843</ItemID>
    <ListingDetails>
      <Adult>false</Adult>
      <BindingAuction>false</BindingAuction>
      <CheckoutEnabled>true</CheckoutEnabled>
      <ConvertedBuyItNowPrice currencyID="USD">10.0</ConvertedBuyItNowPrice>
      <ConvertedStartPrice currencyID="USD">1.0</ConvertedStartPrice>
      <ConvertedReservePrice currencyID="USD">0.0</ConvertedReservePrice>
      <HasReservePrice>false</HasReservePrice>
      <StartTime>2016-08-01T10:02:42.000Z</StartTime>
      <EndTime>2016-08-01T10:14:35.000Z</EndTime>
      <ViewItemURL>http://cgi.sandbox.ebay.com/men-timberland-shoes-/110182207843</ViewItemURL>
      <HasUnansweredQuestions>false</HasUnansweredQuestions>
      <HasPublicMessages>false</HasPublicMessages>
      <ViewItemURLForNaturalSearch>http://cgi.sandbox.ebay.com/men-timberland-shoes-/110182207843</ViewItemURLForNaturalSearch>
    </ListingDetails>
    <ListingDuration>Days_7</ListingDuration>
    <ListingType>Chinese</ListingType>
    <Location>Aylesbury</Location>
    <PaymentMethods>PayPal</PaymentMethods>
    <PayPalEmailAddress>andrew.douglas@eurekasolutions.co.uk</PayPalEmailAddress>
    <PrimaryCategory>
      <CategoryID>11498</CategoryID>
      <CategoryName>Clothing, Shoes &amp; Accessories:Men&apos;s Shoes:Boots</CategoryName>
    </PrimaryCategory>
    <PrivateListing>false</PrivateListing>
    <Quantity>1</Quantity>
    <ReservePrice currencyID="USD">0.0</ReservePrice>
    <ReviseStatus>
      <ItemRevised>true</ItemRevised>
    </ReviseStatus>
    <Seller>
      <AboutMePage>false</AboutMePage>
      <Email>dp_moran@hotmail.com</Email>
      <FeedbackScore>500</FeedbackScore>
      <PositiveFeedbackPercent>0.0</PositiveFeedbackPercent>
      <FeedbackPrivate>false</FeedbackPrivate>
      <FeedbackRatingStar>Purple</FeedbackRatingStar>
      <IDVerified>true</IDVerified>
      <eBayGoodStanding>true</eBayGoodStanding>
      <NewUser>false</NewUser>
      <RegistrationDate>1995-01-01T00:00:00.000Z</RegistrationDate>
      <Site>UK</Site>
      <Status>Confirmed</Status>
      <UserID>testuser_eureka1</UserID>
      <UserIDChanged>false</UserIDChanged>
      <UserIDLastChanged>2014-07-18T08:16:48.000Z</UserIDLastChanged>
      <VATStatus>VATTax</VATStatus>
      <SellerInfo>
        <AllowPaymentEdit>true</AllowPaymentEdit>
        <CheckoutEnabled>true</CheckoutEnabled>
        <CIPBankAccountStored>false</CIPBankAccountStored>
        <GoodStanding>true</GoodStanding>
        <LiveAuctionAuthorized>false</LiveAuctionAuthorized>
        <MerchandizingPref>OptIn</MerchandizingPref>
        <QualifiesForB2BVAT>false</QualifiesForB2BVAT>
        <StoreOwner>false</StoreOwner>
        <SafePaymentExempt>true</SafePaymentExempt>
      </SellerInfo>
      <MotorsDealer>false</MotorsDealer>
    </Seller>
    <SellingStatus>
      <BidCount>1</BidCount>
      <BidIncrement currencyID="USD">0.5</BidIncrement>
      <ConvertedCurrentPrice currencyID="USD">10.0</ConvertedCurrentPrice>
      <CurrentPrice currencyID="USD">10.0</CurrentPrice>
      <HighBidder>
        <AboutMePage>false</AboutMePage>
        <EIASToken>nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wFk4GhDJWApgqdj6x9nY+seQ==</EIASToken>
        <Email>Invalid Request</Email>
        <FeedbackScore>500</FeedbackScore>
        <PositiveFeedbackPercent>0.0</PositiveFeedbackPercent>
        <FeedbackPrivate>false</FeedbackPrivate>
        <FeedbackRatingStar>Purple</FeedbackRatingStar>
        <IDVerified>true</IDVerified>
        <eBayGoodStanding>true</eBayGoodStanding>
        <NewUser>false</NewUser>
        <RegistrationDate>1995-01-01T00:00:00.000Z</RegistrationDate>
        <Site>US</Site>
        <Status>Confirmed</Status>
        <UserID>testuser_eureka2</UserID>
        <UserIDChanged>false</UserIDChanged>
        <UserIDLastChanged>2014-07-18T09:12:17.000Z</UserIDLastChanged>
        <VATStatus>NoVATTax</VATStatus>
        <BuyerInfo>
          <ShippingAddress>
            <Country>US</Country>
            <PostalCode>98102</PostalCode>
          </ShippingAddress>
        </BuyerInfo>
        <UserAnonymized>false</UserAnonymized>
      </HighBidder>
      <LeadCount>0</LeadCount>
      <MinimumToBid currencyID="USD">10.5</MinimumToBid>
      <QuantitySold>1</QuantitySold>
      <ReserveMet>true</ReserveMet>
      <SecondChanceEligible>false</SecondChanceEligible>
      <ListingStatus>Ended</ListingStatus>
      <SoldAsBin>true</SoldAsBin>
      <QuantitySoldByPickupInStore>0</QuantitySoldByPickupInStore>
    </SellingStatus>
    <ShippingDetails>
      <ApplyShippingDiscount>false</ApplyShippingDiscount>
      <CalculatedShippingRate>
        <WeightMajor measurementSystem="English" unit="lbs">0</WeightMajor>
        <WeightMinor measurementSystem="English" unit="oz">0</WeightMinor>
      </CalculatedShippingRate>
      <SalesTax>
        <SalesTaxPercent>0.0</SalesTaxPercent>
        <ShippingIncludedInTax>false</ShippingIncludedInTax>
      </SalesTax>
      <ShippingServiceOptions>
        <ShippingService>StandardShippingFromOutsideUS</ShippingService>
        <ShippingServiceCost currencyID="USD">5.0</ShippingServiceCost>
        <ShippingServicePriority>1</ShippingServicePriority>
        <ExpeditedService>false</ExpeditedService>
        <ShippingTimeMin>5</ShippingTimeMin>
        <ShippingTimeMax>10</ShippingTimeMax>
      </ShippingServiceOptions>
      <ShippingType>Flat</ShippingType>
      <ThirdPartyCheckout>false</ThirdPartyCheckout>
      <ShippingDiscountProfileID>0</ShippingDiscountProfileID>
      <InternationalShippingDiscountProfileID>0</InternationalShippingDiscountProfileID>
      <SellerExcludeShipToLocationsPreference>true</SellerExcludeShipToLocationsPreference>
    </ShippingDetails>
    <ShipToLocations>US</ShipToLocations>
    <Site>US</Site>
    <StartPrice currencyID="USD">1.0</StartPrice>
    <TimeLeft>PT0S</TimeLeft>
    <Title>men timberland shoes</Title>
    <HitCount>0</HitCount>
    <LocationDefaulted>true</LocationDefaulted>
    <GetItFast>false</GetItFast>
    <BuyerResponsibleForShipping>false</BuyerResponsibleForShipping>
    <PostalCode>HP19 3EQ</PostalCode>
    <PictureDetails>
      <PhotoDisplay>None</PhotoDisplay>
    </PictureDetails>
    <DispatchTimeMax>3</DispatchTimeMax>
    <ProxyItem>false</ProxyItem>
    <BuyerGuaranteePrice currencyID="USD">20000.0</BuyerGuaranteePrice>
    <IntangibleItem>false</IntangibleItem>
    <ReturnPolicy>
      <ReturnsAcceptedOption>ReturnsNotAccepted</ReturnsAcceptedOption>
      <ReturnsAccepted>No returns accepted</ReturnsAccepted>
    </ReturnPolicy>
    <PaymentAllowedSite>eBayMotors</PaymentAllowedSite>
    <PaymentAllowedSite>CanadaFrench</PaymentAllowedSite>
    <PaymentAllowedSite>Canada</PaymentAllowedSite>
    <PaymentAllowedSite>US</PaymentAllowedSite>
    <ConditionID>1000</ConditionID>
    <ConditionDisplayName>New with box</ConditionDisplayName>
    <PostCheckoutExperienceEnabled>false</PostCheckoutExperienceEnabled>
    <ShippingPackageDetails>
      <ShippingIrregular>false</ShippingIrregular>
      <ShippingPackage>PackageThickEnvelope</ShippingPackage>
      <WeightMajor measurementSystem="English" unit="lbs">0</WeightMajor>
      <WeightMinor measurementSystem="English" unit="oz">0</WeightMinor>
    </ShippingPackageDetails>
    <HideFromSearch>false</HideFromSearch>
    <eBayPlus>false</eBayPlus>
    <eBayPlusEligible>false</eBayPlusEligible>
  </Item>
</GetItemResponse>"""


# print type(addOrder)

# d = xmltodict.parse(addOrder)
# tid = d['AddOrderRequest']['Order']['TransactionArray']['Transaction'][0]['TransactionID']

# print type(tid)
# print tid

# d = dict(xmltodict.parse(addOrder)['GetOrderTransactionsResponse']['OrderArray']['Order'])
d = dict(xmltodict.parse(getItem)['GetItemResponse']['Item'])
d_j = json.dumps(d, indent=4)

print d_j
# print json.loads(d_j)
