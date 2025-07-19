# Ontology Dev 
This is a generated output of different classes of payments, which is considered to be an initial template advancing from earlier works, only.  




## Ontological Definition: Contribution Classifications & Currencies

This ontology outlines classes representing contributions and currencies, focusing on their characteristics and relationships.  It's structured using a basic class/property hierarchy suitable for knowledge representation (e.g., OWL).  We will use the prefix "co:" for contribution-related terms and "cu:" for currency-related terms.



### I. Contribution Classifications Ontology (co:)

**Root Class: `co:Contribution`**
*   **Definition:** An act of providing something valuable to a project, initiative or goal.  This is the overarching concept.
*   **Properties:**
    *   `co:contributor`:  Individual or entity making the contribution (Data Property - link to Person/Organization class).
    *   `co:contributionDate`: Date of the contribution (Data Property – DateTime)
    *   `co:effortEstimate`: Estimated effort required for the contribution (Data Property – numerical value with units, e.g., hours)
    * `co:actualEffort`: Actual effort expended on the contribution (Data Property - numerical value with units)
    *   `co:description`: Textual description of the contribution (Data Property – String)
    *   `co:project` : Project to which the contribution is made (Object property, link to Project class).

**Subclasses:**

1.  **`co:NecessaryContribution`** (SubclassOf `co:Contribution`)
    *   **Definition:** Contribution essential for project completion/success.
    *   **Properties:** `co:requiredBy`: Task or deliverable requiring this contribution.

2.  **`co:UnsolicitedContribution`** (SubclassOf `co:Contribution`)
    *   **Definition:** Contribution made without prior request.
    *   **Properties:** None specific beyond those of `co:Contribution`.

3.  **`co:ValuedContribution`** (SubclassOf `co:Contribution`)
    *   **Definition:** Contribution recognized as beneficial.
    *   **Properties:** `co:valueAssessment`: Result of feedback/evaluation process (Data Property – String/Numerical).

4.  **`co:CollaborativeContribution`** (SubclassOf `co:Contribution`)
    *   **Definition:** Contribution involving teamwork or shared effort.
    *   **Properties:** `co:collaborators`: List of individuals involved in collaboration (Object property - link to Person class)

5.  **`co:TimeLimitedContribution`** (SubclassOf `co:Contribution`)
    *   **Definition:** Contribution performed within a specified timeframe.
    *   **Properties:** `co:duration`: Length of the contribution period (Data Property – Duration).

6.  **`co:OngoingContribution`** (SubclassOf `co:Contribution`)
    *   **Definition:** Contribution provided over an extended duration.
    *   **Properties:** `co:startDate`: Date the ongoing contribution began (Data Property - DateTime)

7.  **`co:DiscreteContribution`** (SubclassOf `co:Contribution`)
    *   **Definition:** Self-contained contribution, independent of others.
    *   **Properties:** None specific beyond those of `co:Contribution`.

8.  **`co:InterdependentContribution`** (SubclassOf `co:Contribution`)
    *   **Definition:** Contribution reliant on other contributions.
    *   **Properties:** `co:dependsOn`: List of contributions required for this contribution to be completed (Object property - link to `co:Contribution`).

9.  **`co:DesignWork`**, **`co:Research`**, **`co:Programming`**, **`co:Testing`**: (SubclassesOf `co:Contribution`) – These represent specific *types of work*, inheriting all properties of `co:Contribution`.

10. **`co:ResourceContribution`** (SubclassOf `co:Contribution`)
    *   **Definition:** Contribution of physical or digital resources.
    *   **Properties:**  `co:resourceType`: Type of resource contributed (Data Property – String, e.g., “Software”, “Hardware”).

11. **`co:IntellectualPropertyContribution`** (SubclassOf `co:Contribution`)
    *   **Definition:** Contribution of IP rights or assets.
    *   **Properties:** `co:ipType`: Type of intellectual property (Data Property – String, e.g., “Patent”, “Trademark”).

12. **`co:DefinedTermsContribution`** (SubclassOf `co:Contribution`)
    *   **Definition:** Contribution made under specific legal conditions.
    *   **Properties:**  `co:license`: License governing the contribution (Data Property - link to License class).

13. **`co:ExpertiseBasedContribution`** (SubclassOf `co:Contribution`)
    *   **Definition:** Contribution based on specialized knowledge.
    *   **Properties:** `co:expertiseArea`: Field of expertise (Data Property – String).

14. **`co:RoleBasedContribution`** (SubclassOf `co:Contribution`)
    *   **Definition:** Contributions related to a specific role within the project.
    *   **Properties:** `co:role`: Role associated with this contribution (Data Property - link to Role class).

15. **Redundant Classification**:  The 15th and 16th classifications repeat functionality already covered by `co:CollaborativeContribution` & `co:DiscreteContribution`.



### II. Financial and Non-Financial Currencies Ontology (cu:)

**Root Class: `cu:Currency`**
*   **Definition:** A medium of exchange for goods, services or value.
*   **Properties:**
    *   `cu:name`: Name of the currency (Data Property – String).
    *   `cu:symbol`: Currency symbol (Data Property - String)
    *   `cu:unitOfMeasure`: Unit used to measure this currency (Data Property-String, e.g., USD, time unit, carbon credit).

**Subclasses:**

#### A. Financial Currencies (cu:FinancialCurrency)** (SubclassOf `cu:Currency`)

1.  **`cu:MicroPayment`** (SubclassOf `cu:FinancialCurrency`)
    *   **Definition:** Small online payments.

2.  **`cu:Gift`** (SubclassOf `cu:FinancialCurrency`)
    *   **Definition:** Payment without expectation of return.
    *   **Properties:** `co:purpose`: Reason for the gift (Data Property - String).

3.  **`cu:Donation`** (SubclassOf `cu:FinancialCurrency`)
    *   **Definition:** Payment to support a cause/organisation.
    *   **Properties:** `cu:recipientOrganization`: Organization receiving donation (Object property – Link to Organization class)

4.  **`cu:SubscriptionPayment`** (SubclassOf `cu:FinancialCurrency`)
    *   **Definition:** Regular payment for access to service/product.

5.  **`cu:InstalmentPayment`** (SubclassOf `cu:FinancialCurrency`)
    *   **Definition:** Payment made over time.

6.  **`cu:SalaryWage`** (SubclassOf `cu:FinancialCurrency`)
    *   **Definition:** Payment for work performed.

7. **... and the rest of Financial Classes from the document ...** - These would be similarly defined as subclasses of `cu:FinancialCurrency`.

#### B. Non-Financial Currencies (cu:NonFinancialCurrency)** (SubclassOf `cu:Currency`)

1.  **`cu:TimeBankCredit`** (SubclassOf `cu:NonFinancialCurrency`)
    *   **Definition:** Credit earned through service exchange in a time bank.
    *   **Properties:** `cu:timeUnit`: Unit of time representing the credit (Data Property – String, e.g., “hour”).

2.  **`cu:LoyaltyPoint`**(SubclassOf `cu:NonFinancialCurrency`)
    *   **Definition:** Points earned through customer loyalty programs.
    * **Properties**: `co:loyaltyProgram`: The program associated with these points (Object Property - Link to Program class)

3.  **`cu:SocialCurrency`** (SubclassOf `cu:NonFinancialCurrency`)
    *   **Definition:** Value derived from social connections/relationships.

4. **... and the rest of Non-Financial Classes from the document ...** – These would be similarly defined as subclasses of `cu:NonFinancialCurrency`.



#### C. Biosphere Related Currencies (cu:BiosphereCurrency)** (SubclassOf cu:NonFinancialCurrency)
    *   **Definition**:  A non financial currency that relates to the natural environment

1. **`cu:CarbonCredit`** (SubclassOf `cu:BiosphereCurrency`)
    *  **Definition**: A type of credit used to offset carbon dioxide emissions. 
2. **... and other biosphere classes from document ...** - These would be similarly defined as subclasses of `cu:BiosphereCurrency`.

#### D. SocioSphere Related Currencies (cu:SocioSphereCurrency)**(SubclassOf cu:NonFinancialCurrency)
    *   **Definition**: A non financial currency that relates to society and social good. 
3. **`cu:VolunteerCredit`**(SubclassOf `cu:SocioSphereCurrency`)
    *  **Definition**: Credit earned through volunteering or other forms of community service.
4. **... and other sociosphere classes from document ...** - These would be similarly defined as subclasses of `cu:SocioSphereCurrency`.

**Important Notes:**

*   This is a high-level ontology. Each class can have further subclasses and properties for more detailed representation.
*   Relationships between contribution types and currencies are crucial.  For example, a `co:UnsolicitedContribution` might be *rewarded with* a `cu:LoyaltyPoint`. This relationship would need to be modeled using appropriate object properties (e.g., `co:rewards`, `cu:earnedThrough`).
*   Taxation and Fees are best represented as classes related to financial transactions, not currencies themselves.  They represent attributes *of* those transactions.


This ontological structure provides a foundation for representing contributions, their characteristics, and various forms of currency used to acknowledge or exchange value within projects and communities. The use of OWL and similar knowledge representation languages enables reasoning and automated analysis based on these definitions.


Input Refernece;

define the following in an ontological format, 

1. ## Contribution Classifications

There is a need to create categories in relation to the types of contributions made. Some may be as simple as a small change, that takes a few seconds; others, may represent on-going works over a long-period of time; that has involved great sacrifice & attention. 

In some cases also; contributions may be specifically requested; whilst others, may just be an idea or something that someone thought was a ‘good idea’, and they just did it.   The means to create formula around how to address the characteristics of any, requires the framework to be defined; here are some initial thoughts,

1. **Necessary contributions:** These are contributions that are identified as necessary for the successful completion of a project. They may involve tasks or responsibilities that are specifically assigned to individuals or that are essential for the project to move forward.

   2. **Unsolicited contributions:** These are contributions that are made by individuals without being specifically requested or assigned. They may be undertaken on a volunteer basis or as part of an individual's personal interest in the project.

   3. **Valued contributions:** These are contributions that are considered to be particularly valuable or beneficial to the project. They may be identified through feedback or evaluation processes, or through other means of assessment.

   4. **Collaborative contributions:** These are contributions that involve collaboration or teamwork with others. They may involve the exchange of ideas, the sharing of resources or expertise, or other forms of collaboration.

   5. **Time-limited contributions:** These are contributions that are made on a temporary or short-term basis. They may involve tasks or responsibilities that are specific to a particular phase or stage of the project, or that are completed within a specific timeframe.

   6. **Ongoing contributions:** These are contributions that are made on a more long-term or ongoing basis. They may involve tasks or responsibilities that are ongoing or that are expected to continue over a longer period of time.

   7. **Discrete contributions:** These are contributions that are self-contained or that can be completed independently of other contributions. They may involve tasks or responsibilities that are discrete or that can be completed on a standalone basis.

   8. **Interdependent contributions:** These are contributions that are dependent on or interconnected with other contributions. They may involve tasks or responsibilities that rely on the work of others in order to be completed or that are part of a larger system or process.

   9. **Different types of work:** This classification could involve subcategories for different types of tasks or responsibilities, such as design work, research, programming, testing, etc.

   10. **Contributions of resources or equipment and supplies:** This classification could involve subcategories for different types of resources or supplies that are contributed to the project, such as software, hardware, data, etc.

   11. **Contributions of intellectual property:** This classification could involve subcategories for different types of intellectual property contributions, such as patents, trademarks, copyrights, etc.

   12. **Contributions on defined terms:** This classification could involve subcategories for contributions that are made on specific terms or conditions, such as contributions made under a particular licence or agreement.

   13. **Expertise-based contributions:** This classification could involve subcategories for contributions that are based on specific expertise or skills, such as contributions of knowledge or expertise in a particular field or domain.

   14. **Role-based contributions:** This classification could involve subcategories for contributions that are related to specific roles or responsibilities, such as contributions made by project managers, team leaders, or other key stakeholders.

   15. **Collaborative contributions:** This classification could involve subcategories for contributions that involve collaboration or teamwork with others, such as contributions that involve the exchange of ideas or the sharing of resources or expertise.

   16. **Standalone contributions:** This classification could involve subcategories for contributions that are self-contained or that can be completed independently of other contributions, such as contributions that are discrete or that can be completed on a standalone basis.

2. ## Financial and non-financial currencies 

There are many different types of ‘transactional events’ that can be associated with instruments of some-kind, that may directly or indirectly result in payments or different forms of acknowledgement or other related socio-economic methods, measures & supports.  These systems are made in various contexts, including: which are hereby provided some basic initial outlines, per below.  These works will in-turn need to be transcribed into a functional technical system & related modelling, built using ontologies, various forms of cryptographic instruments and related tooling; including, blockchain tools.

### Financial 

#### General

1. **Micro Payments**: These are small payments that are typically made online and are used to purchase digital goods or services. They are often used for low-cost items or for items that are purchased frequently, such as online articles or music tracks.

   Micropayment systems are a critical component of how the requirements for various systems are going to be made able to work. However the design of these systems must consider various ESG factors \- which is part of what the intention of ensuring support for micropayments does innately; but that also, the Biosphere Ontologies and in-particular Energy Calcs become critically important. 

   The way through which micropayment mechanisms are made able to work, must end-up costing less than the amount of the payment.

2. **Gifts And Donations**: These are payments that are made without the expectation of receiving something in return. Gifts are typically given to show affection or appreciation, while donations are often made to support a particular cause or organisation. There are a few key differences between gifts and donations:

   1. **Purpose**: Gifts are typically given for personal reasons, such as to show appreciation or affection, while donations are typically given to support a particular cause or organisation.

   2. **Recipient**: Gifts are typically given to individuals, while donations are typically given to organisations or causes.

   3. **Tax implications**: In some cases, gifts may be subject to gift tax, depending on the value of the gift and the relationship between the giver and the recipient. Donations, on the other hand, may be tax-deductible in some cases, depending on the nature of the organisation receiving the donation and the specific tax laws in the giver's jurisdiction.

   4. **Expectation of return**: Gifts are typically given without any expectation of receiving anything in return, while donations may be given in exchange for certain benefits, such as recognition or access to special events or resources.

Gifts and Donations differ in terms of their purpose, recipient, and potential tax implications; but are both forms of voluntary payments that are made freely and without any expectation of receiving anything in return.

3. **Subscription payments**: These are payments that are made on a regular basis, such as monthly or annually, in exchange for access to a particular service or product.

4. **Instalment payments**: These are payments that are made over a period of time, rather than in a single lump sum. They may be used to purchase larger items or services, such as a car or a home.

5. **Salary or wages**: These are payments that are made to employees in exchange for their work. They may be based on an hourly rate, a yearly salary, or some other form of compensation.

6. **Royalties**: These are payments that are made to individuals or organisations for the use of their intellectual property, such as patents, trademarks, or copyrights.

7. **Licensing fees**: These are payments that are made in exchange for the right to use a particular product or service. They may be paid on a one-time basis or on a regular basis, such as annually.

8. **Commission**: These are payments that are made to individuals or organisations for their efforts in selling a product or service. They may be based on a percentage of the sale price or on some other form of compensation.

9. **Dividends**: These are payments that are made to shareholders in a company as a distribution of the company's profits.

10. **Rent**: These are payments that are made in exchange for the use of a particular property, such as an apartment or a piece of land.

11. **Loans**: These are payments that are made to individuals or organisations to borrow money, with the expectation that the money will be repaid with interest at a later date.

12. **Grants**: These are payments that are made to individuals or organisations to support a particular project or initiative. Grants may be provided by government agencies, foundations, or other organisations and may have specific terms and conditions attached to their use.

13. **Scholarships**: These are payments that are made to students to help cover the cost of education. Scholarships may be based on merit, financial need, or other criteria and may be provided by schools, universities, or other organisations.

14. **Bursaries**: These are payments that are made to students to help cover the cost of education and are typically based on financial need. Bursaries may be provided by schools, universities, or other organisations.

15. **Insurance payments**: These are payments that are made by individuals or organisations to cover the cost of insurance premiums. Insurance payments may be made on a regular basis, such as monthly or annually, and may cover a wide range of risks, including health, property, and liability.

16. **Tips**: These are payments that are made to individuals who provide a service, such as a waiter, hairdresser, or taxi driver. Tips are typically given as a way to show appreciation or gratitude for good service.

#### Taxation

17. **Sales tax**: These are payments that are made on the purchase of goods or services and are typically collected by the seller on behalf of the government. Sales tax rates vary by jurisdiction and may be based on a percentage of the purchase price.

18. **Value-added tax (VAT)**: This is a type of consumption tax that is applied to the sale of goods and services. VAT rates vary by jurisdiction and may be based on a percentage of the sale price.

19. **Property tax**: These are payments that are made on the ownership of property, such as a home or a piece of land. Property tax rates vary by jurisdiction and may be based on the value of the property.

20. **Business tax**: These are payments that are made by businesses on the profits or income they generate. Business tax rates vary by jurisdiction and may be based on a percentage of the business's profits or income.

21. **Personal tax**: These are payments that are made by individuals on their income or wealth. Personal tax rates vary by jurisdiction and may be based on a progressive scale, with higher rates applying to higher levels of income or wealth.

22. **Excise tax**: These are taxes that are applied to specific goods or services, such as gasoline, tobacco, or alcohol. Excise tax rates may vary by jurisdiction and may be based on the quantity or value of the goods or services.

23. **Import tax**: These are taxes that are applied to goods that are imported into a country. Import tax rates may vary by jurisdiction and may be based on the value or quantity of the goods being imported.

24. **Export tax**: These are taxes that are applied to goods that are exported from a country. Export tax rates may vary by jurisdiction and may be based on the value or quantity of the goods being exported.

25. **Payroll tax**: These are taxes that are applied to the wages or salaries of employees and are typically collected by the employer on behalf of the government. Payroll tax rates may vary by jurisdiction and may be based on a percentage of the employee's wages or salary.

#### Fees

26. **Usage fees**: These are fees that are charged for the use of a particular service or product. Usage fees may be based on the amount of time or resources used or on some other metric.

27. **Transaction fees**: These are fees that are charged for processing a financial transaction, such as a credit card payment or a bank transfer. Transaction fees may be based on a percentage of the transaction amount or on a flat rate.

28. **Service charges**: These are fees that are charged for services rendered, such as legal or consulting services. Service charges may be based on an hourly rate or on a flat fee.

29. **Membership fees**: These are fees that are charged for membership in a particular organisation or club. Membership fees may be based on a flat rate or on a recurring basis, such as annually.

30. **Penalty fees**: These are fees that are charged for failing to meet certain obligations or requirements, such as late payment fees or overdraft fees.

31. **Court fees**: These are fees that are charged for the use of court facilities or for other legal services. Court fees may be based on a flat rate or on a percentage of the amount in dispute.

32. **Registration fees**: These are fees that are charged for the registration of a particular item, such as a vehicle or a trademark. Registration fees may be based on a flat rate or on a percentage of the value of the item being registered.

33. **Permit fees**: These are fees that are charged for the issuance of a permit, such as a building permit or a hunting or fishing licence. Permit fees may be based on a flat rate or on a percentage of the value of the activity being permitted.

34. **Access fees**: These are fees that are charged for access to a particular service or resource, such as an online database or a gym membership. Access fees may be based on a flat rate or on a recurring basis, such as monthly.

35. **Transfer fees**: These are fees that are charged for the transfer of a particular asset or liability, such as a real estate transaction or a stock trade. Transfer fees may be based on a flat rate or on a percentage of the value of the asset or liability being transferred.

36. **Processing fees**: These are fees that are charged for the processing of a particular request or application, such as a passport application or a loan application. Processing fees may be based on a flat rate or on a percentage of the value of the request or application.

37. **Maintenance fees**: These are fees that are charged for the maintenance or upkeep of a particular asset or service, such as a software subscription or a gym membership. Maintenance fees may be based on a flat rate or on a recurring basis, such as annually.

38. **Upgrade fees**: These are fees that are charged for the upgrade of a particular product or service, such as a software upgrade or a cell phone plan upgrade. Upgrade fees may be based on a flat rate or on a percentage of the value of the upgrade.

39. **Exit fees**: These are fees that are charged for the termination of a particular service or contract, such as a cell phone contract or a rental agreement. Exit fees may be based on a flat rate or on a percentage of the value of the service or contract.

40. **Penalty interest**: These are additional interest charges that are applied when a payment is late or when a financial obligation is not met. Penalty interest rates may be based on a percentage of the unpaid amount or on a flat rate.

41. **Late fees**: These are fees that are charged for the late payment of a particular obligation, such as a rent payment or a credit card payment. Late fees may be based on a flat rate or on a percentage of the unpaid amount.

42. **Overdue fees**: These are fees that are charged for the failure to return an item by a certain date, such as a library book or a rented movie. Overdue fees may be based on a flat rate or on a daily or weekly basis.

43. **Restocking fees**: These are fees that are charged for the return of a product that has been opened or used, such as a software program or an electronic device. Restocking fees may be based on a percentage of the purchase price or on a flat rate.

44. **Service charges**: These are fees that are charged for the use of a particular service, such as a hotel room service charge or a restaurant service charge. Service charges may be based on a percentage of the total bill or on a flat rate.

45. **Credit card fees**: These are fees that are charged for the use of a credit card, such as annual fees, balance transfer fees, or cash advance fees. Credit card fees may be based on a flat rate or on a percentage of the transaction amount.

#### Other

46. **Security deposits**: These are payments that are made upfront to secure the use of a particular asset or service, such as a rental property or a storage unit. Security deposits may be refundable or non-refundable, depending on the terms of the agreement.

47. **Rent payments**: These are payments that are made for the use of a particular property, such as a home or an office. Rent payments may be based on a flat rate or on a percentage of the value of the property.

48. **Lease payments**: These are payments that are made for the use of a particular asset, such as a car or equipment. Lease payments may be based on a flat rate or on a percentage of the value of the asset.

49. **Loan payments**: These are payments that are made to repay a loan, such as a mortgage or a personal loan. Loan payments may be based on a fixed interest rate or on a variable interest rate.

50. **Utility payments**: These are payments that are made for the use of a particular service, such as electricity, water, or gas. Utility payments may be based on a flat rate or on a usage-based rate.

51. **Dues**: These are payments that are made for membership in an organisation or association, such as a professional association or a social club. Dues may be based on a flat rate or on a recurring basis, such as annually.

Overall, there are many different types of payments that can be made in various contexts, depending on the specific needs and circumstances of the parties involved.

### Non-Financial 

*(Knowledge Economy ‘Currencies’)*

There are many types of non-financial currencies that can be used in place of traditional financial currencies, such as dollars, euros, or pounds. Non-financial currencies can take a variety of forms and can be used for a variety of purposes.

It is worth noting that non-financial currencies can be used in a variety of ways and can have a variety of benefits. For example, non-financial currencies may:

* Provide an alternative means of exchange in situations where traditional financial currencies are not available or are not practical.

* Encourage local economic development and community building by promoting trade within a specific community or region.

* Foster loyalty and reward customer behaviour.

* Create new opportunities for innovation and experimentation with different forms of value exchange.

Traditionally; non-financial currencies have also had an array of limitations and challenges.

For example:

* Be subject to fraud or abuse.

* Be difficult to track and audit.

* Be subject to volatility and fluctuation in value.

* Be subject to regulation and oversight by governments or other authorities.

As such, whilst non-financial currencies can be a useful and innovative way to exchange value and facilitate transactions, it is important to carefully consider the potential benefits and challenges before implementing them. One of the more significant recent examples is Carbon Credits.  Carbon credits are a type of non-financial currency that can be bought and sold as a way to offset carbon dioxide emissions. Carbon credits are used as a way to incentivize the reduction of greenhouse gas emissions and to promote the adoption of clean energy technologies.

Under a carbon credit system, a government or other authority sets a cap on the amount of carbon dioxide that can be emitted within a specific region or sector. Companies or other organisations that exceed their allocated carbon emissions are required to purchase carbon credits from those that have emitted less than their allocated amount. This creates a market for carbon credits, with the goal of reducing overall carbon dioxide emissions and incentivizing the adoption of clean energy technologies.

Carbon credits can be bought and sold on carbon markets, such as the European Union Emissions Trading System (EU ETS) or the Chicago Climate Exchange (CCX). The value of carbon credits is typically based on the cost of reducing or offsetting a ton of carbon dioxide emissions.

Overall, carbon credits are a way to use market forces to encourage the reduction of greenhouse gas emissions and the adoption of clean energy technologies.

Some other examples of non-financial currencies might include:

52. **Time banks**: Time banks are systems in which people exchange services with one another, using time as the currency. For example, someone might trade an hour of gardening for an hour of computer repair.

53. **Loyalty points**: Many businesses offer loyalty points as a way to reward customer loyalty. These points can be redeemed for goods or services at a later date.

54. **Social currency:** Social currency refers to the value that is derived from social connections or relationships. For example, someone might offer a favour to a friend in exchange for a favour at a later date.

55. **Alternative currencies**: Alternative currencies are currencies that are created and used outside of the traditional financial system. Examples might include barter systems or digital currencies such as Bitcoin.

56. **Reputation points**: Some online communities use reputation points as a way to reward and recognize contributions. These points might be visible on a user's profile or might be used to unlock special privileges or perks.

57. **Coupons**: Coupons are a type of non-financial currency that can be exchanged for goods or services at a later date. Coupons may be issued by businesses or may be obtained through loyalty programs or other promotions.

58. **Gift cards**: Gift cards are a type of non-financial currency that can be used to purchase goods or services at a later date. Gift cards may be issued by businesses or may be purchased by individuals as a gift for someone else.

59. **Air miles**: Air miles are a type of non-financial currency that can be earned through the use of certain credit cards or loyalty programs. Air miles can be redeemed for flights or other travel-related benefits.

60. **Points**: Points are a type of non-financial currency that can be earned through the use of certain credit cards, loyalty programs, or other promotions. Points can be redeemed for a variety of goods and services, such as merchandise, gift cards, or travel-related benefits.

61. **Credits**: Credits are a type of non-financial currency that can be earned through the use of certain online platforms or services. Credits can be used to purchase goods or services within the platform or may be exchangeable for other types of currencies.

62. **Tickets**: Tickets are a type of non-financial currency that can be exchanged for goods or services at a later date. Tickets may be used to purchase admission to events, such as concerts or sporting events, or to access certain amenities, such as amusement park rides.

63. **Vouchers**: Vouchers are a type of non-financial currency that can be exchanged for goods or services at a later date. Vouchers may be issued by businesses or may be obtained through loyalty programs or other promotions.

64. **Tokens**: Tokens are a type of non-financial currency that can be used to purchase goods or services within a specific context, such as at a carnival or an arcade.

65. **Community currencies**: Community currencies are a type of non-financial currency that is used within a specific community or region. These currencies may be used to facilitate trade or to promote local economic development.

66. **Virtual currencies**: Virtual currencies are a type of non-financial currency that exists entirely online. Examples might include digital currencies such as Bitcoin or in-game currencies used within online gaming platforms.

#### Biosphere

There are many types of non-financial currencies that are related to the biosphere or the natural environment. Some examples might include:

67. **Water credits:** Water credits are a type of non-financial currency that can be bought and sold as a way to incentivize the efficient use of water resources. Water credits may be used to allocate water rights or to offset water use in different regions or sectors.

68. **Biodiversity credits:** Biodiversity credits are a type of non-financial currency that can be bought and sold as a way to incentivize the conservation of biodiversity and the protection of ecosystems. Biodiversity credits may be used to offset the impact of development projects or to reward the implementation of conservation measures.

69. **Carbon offset credits:** Carbon offset credits are a type of non-financial currency that can be bought and sold as a way to offset carbon dioxide emissions. Carbon offset credits may be used to offset the carbon emissions of a specific project or activity by supporting the implementation of carbon reduction projects elsewhere.

70. **Ecological credits:** Ecological credits are a type of non-financial currency that can be bought and sold as a way to incentivize the restoration and protection of ecosystems. Ecological credits may be used to offset the impact of development projects or to reward the implementation of conservation measures.

71. **Nature credits:** Nature credits are a type of non-financial currency that can be bought and sold as a way to incentivize the conservation of natural resources and the protection of the environment. Nature credits may be used to offset the impact of development projects or to reward the implementation of conservation measures.

72. **Eco-points:** Eco-points are a type of non-financial currency that can be earned through the adoption of environmentally-friendly behaviours or the use of eco-friendly products. Eco-points may be redeemable for a variety of goods and services or may be used to unlock special privileges or perks.

73. **Green dollars:** Green dollars are a type of non-financial currency that is used within a specific community or region to promote local economic development and sustainability. Green dollars may be earned through the adoption of environmentally-friendly behaviours or the use of eco-friendly products and may be used to purchase goods and services within the community.

74. **Renewable energy credits:** Renewable energy credits are a type of non-financial currency that can be bought and sold as a way to incentivize the adoption of renewable energy technologies. Renewable energy credits may be used to offset the use of non-renewable energy sources or to reward the generation of renewable energy.

75. **Waste credits:** Waste credits are a type of non-financial currency that can be bought and sold as a way to incentivize the reduction of waste and the adoption of recycling and other waste management practices. Waste credits may be used to offset the generation of waste or to reward the implementation of waste reduction measures.

76. **Green bonds**: Green bonds are a type of financial instrument that is used to raise capital for environmental projects or initiatives. Green bonds may be issued by governments, businesses, or other organisations and may be used to finance a variety of projects, such as renewable energy projects or conservation efforts.

77. **Carbon offsets:** Carbon offsets are a type of non-financial currency that can be bought and sold as a way to offset carbon dioxide emissions. Carbon offsets may be used to offset the carbon emissions of a specific project or activity by supporting the implementation of carbon reduction projects elsewhere.

78. **Eco-tokens:** Eco-tokens are a type of non-financial currency that is used to reward the adoption of environmentally-friendly behaviours or the use of eco-friendly products. Eco-tokens may be redeemable for a variety of goods and services or may be used to unlock special privileges or perks.

79. **Carbon credits for soil carbon sequestration:** Carbon credits could be used to incentivize the adoption of practices that sequester carbon in soil, such as regenerative agriculture or agroforestry.

80. **Water quality credits:** Water quality credits could be used to incentivize the improvement of water quality in lakes, rivers, and other water bodies.

81. **Habitat credits:** Habitat credits could be used to incentivize the creation or restoration of habitat for endangered species or other wildlife.

82. **Ecosystem services credits:** Ecosystem services credits could be used to incentivize the protection of natural systems that provide important benefits to humans, such as flood control, air purification, or pollination.

Within the sphere of ‘knowledge based currencies’, non-financial biosphere-related instruments can be useful to incentivize the conservation of natural resources and protection of our biosphere environment, as well as to promote the adoption of sustainable practices, through the use of technologies that provide a means to value it.

#### SocioSphere

Non-financial sociosphere currencies are a type of non-financial currency that is used to incentivize the adoption of socially-beneficial behaviours or the use of socially-beneficial products and services. Some examples of non-financial sociosphere currencies might include:

83. **Social impact bonds:** Social impact bonds are a type of financial instrument that is used to raise capital for social projects or initiatives. Social impact bonds may be issued by governments, businesses, or other organisations and may be used to finance a variety of projects, such as education initiatives or social services programs.

84. **Volunteer credits:** Volunteer credits are a type of non-financial currency that is earned through volunteering or other forms of community service. Volunteer credits may be redeemable for a variety of goods and services or may be used to unlock special privileges or perks.

85. **Time banks:** Time banks are a type of non-financial currency that is used to exchange services within a community. Time banks may be based on the concept of time credits, with each hour of service earning one time credit that can be used to receive a service from another member of the time bank.

86. **Community service credits:** Community service credits are a type of non-financial currency that is earned through the completion of community service projects or other forms of volunteering. Community service credits may be redeemable for a variety of goods and services or may be used to unlock special privileges or perks.

87. **Social points:** Social points are a type of non-financial currency that is earned through the adoption of socially-beneficial behaviours or the use of socially-beneficial products. Social points may be redeemable for a variety of goods and services or may be used to unlock special privileges or perks.

88. **Community currency:** Community currency is a type of non-financial currency that is used within a specific community or region to promote local economic development and social cohesion. Community currency may be earned through the adoption of socially-beneficial behaviours or the use of socially-beneficial products and may be used to purchase goods and services within the community.

89. **Social capital credits:** Social capital credits are a type of non-financial currency that is earned through the participation in social or community activities. Social capital credits may be redeemable for a variety of goods and services or may be used to unlock special privileges or perks.

90. **Impact tokens:** Impact tokens are a type of non-financial currency that is used to reward the adoption of socially-beneficial behaviours or the use of socially-beneficial products. Impact tokens may be redeemable for a variety of goods and services or may be used to unlock special privileges or perks.

91. **Good deeds credits:** Good deeds credits are a type of non-financial currency that is earned through the completion of good deeds or acts of kindness. Good deeds credits may be redeemable for a variety of goods and services or may be used to unlock special privileges or perks.

92. **Social impact tokens**: Social impact tokens are a type of non-financial currency that is used to reward the adoption of socially-beneficial behaviours or the use of socially-beneficial products. Social impact tokens may be redeemable for a variety of goods and services or may be used to unlock special privileges or perks.

93. **Community service points:** Community service points are a type of non-financial currency that is earned through the completion of community service projects or other forms of volunteering. Community service points may be redeemable for a variety of goods and services or may be used to unlock special privileges or perks.

94. **Social action credits**: Social action credits are a type of non-financial currency that is earned through the participation in social or community activities. Social action credits may be redeemable for a variety of goods and services or may be used to unlock special privileges or perks.

95. **Social responsibility credits:** Social responsibility credits are a type of non-financial currency that is earned through the adoption of socially-responsible behaviours or the use of socially-responsible products. Social responsibility credits may be redeemable for a variety of goods and services or may be used to unlock special privileges or perks.

96. **Impact points:** Impact points are a type of non-financial currency that is earned through the adoption of behaviours or the use of products that have a positive impact on society or the environment. Impact points may be redeemable for a variety of goods and services or may be used to unlock special privileges or perks.

97. **Social enterprise credits:** Social enterprise credits are a type of non-financial currency that is earned through the support of socially-conscious businesses or organisations. Social enterprise credits may be redeemable for a variety of goods and services or may be used to unlock special privileges or perks.

98. **Community involvement credits:** Community involvement credits are a type of non-financial currency that is earned through the participation in community events or activities. Community involvement credits may be redeemable for a variety of goods and services or may be used to unlock special privileges or perks.

99. **Social contribution points**: Social contribution points are a type of non-financial currency that is earned through the completion of social or community service projects. Social contribution points may be redeemable for a variety of goods and services or may be used to unlock special privileges or perks.

100. **Social engagement credits:** Social engagement credits are a type of non-financial currency that is earned through the participation in social or community activities. Social engagement credits may be redeemable for a variety of goods and services or may be used to unlock special privileges or perks.

101. **Social responsibility tokens**: Social responsibility tokens are a type of non-financial currency that is used to reward the adoption of socially-responsible behaviours or the use of socially-responsible products. Social responsibility tokens may be redeemable for a variety of goods and services or may be used to unlock special privileges or perks.

102. **Community involvement tokens:** Community involvement tokens are a type of non-financial currency that is used to reward participation in community events or activities. Community involvement tokens may be redeemable for a variety of goods and services or may be used to unlock special privileges or perks.
+