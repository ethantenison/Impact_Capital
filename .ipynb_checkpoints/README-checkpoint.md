# The Impact of Resource Diversification and Resource Dependence on Young Nonprofits


**Research Objective**
<br />

The aim of this research project is to analyze the impact of resource diversification and resource dependence on young nonprofits. 
<br />

**Background**

<br />

The nonprofit sector in the United States is huge, representing more than \$1 trillion dollars, or 5.6 percent of the US economy. Due to the limited social safety net, many communities rely on nonprofits for social services including healthcare, education, religious services, and housing assistance. It is no secret however that nonprofits are often financial unstable. In fact, based on a survey conducted by the Nonprofit Financial Fund in 2018, 50% of nonprofits are either in a financial deficit or barely breaking even, and this is even more of a concern for young nonprofits.

<br />

Among nonprofit finance scholars, a consensus has formed that maintaining stable and diverse funding sources promotes financial sustainability and autonomous decision making.  This is especially true for large well-established nonprofits. For young and small nonprofits this might not be the case. In fact, diversifying too quickly can be disastrous. The infrastructure needed to maintain diverse funding streams—such as fundraising for private donations, locating, and applying for grants, and handling the documentation requirements of government grants and contracts—can be overwhelming and expensive.  
<br />

Previous studies on the topic have suffered from a lack of data. This is because the IRS has made it as difficult as possible to analyze nonprofit tax forms, called 990’s. Despite being forced by court order in 2015 to publish all 990 e-filings, knowledge of R or Python is essentially required to do any in depth analysis.  In order to overcome this hurdle, I spent the summer developing an algorithm, along with Rushil Udani, to parse the data into a format conducive for data analysis.  
<br />

**Methods**

<br />

My research will use mixed effects logistic regression, random forest, and XGBoost. The dependent variable is going to be nonprofit termination, which is a binary variable located in the 990 forms. Other environment variables included in the dataset will be independent variables. These include assets, liabilities, and the sum of different revenue sources among many others. In addition, I am going to create several independent variables. The first is going to be an index of resource diversification based on the normalized Hirschman–Herfindahl Index, that takes into account the full range of revenue reported from government and private contributions, as well as other revenue-generating activities like fees for service and rental income.  To measure resource dependence, I am going to create ratios of resource revenue to total revenue that will show by how much a nonprofit depends on any one resource. 

<br />

**Expected Results** 

The ultimate goals of this project are to help nonprofits make wise early financial decisions. I think the results will show that young nonprofits do not benefit from resource diversification like well-established ones do. In addition, I think the impact of resource dependence will vary by funding type. Dependence on resources that are more reliable, such as government grants, may not have as negative an impact on nonprofit sustainability, whereas resources that are more volatile, such as program service fees, may be more so. These findings will add to the literature on nonprofit finance, and I also hope to create a Tableau workbook that can be used by academics and policy makers to inform their research. 
