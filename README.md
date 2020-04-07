# sars-cov-2-data-modeling
This repo contains resources for modeling the spread of SARS-COV-2

# What factors influence the spread of SARS-COV-2?

### Working from base truths, upward. We have our infection conditions:
* This virus can only spread by bringing an infected host in close contact (roughly 6ft or less) with a non-infected host.
* There may be transmission through contact with a surface soon after an infected host had contact with the same surface, so we might have to take that into account.
  * Note: the CDC says it is possible to spread this way, but it is not thought to be the main way the virus spreads.
  * SOURCE: https://www.cdc.gov/coronavirus/2019-ncov/prepare/transmission.html

What needs to be done is we must deduce every factor we can think of which creates one or both of the above conditions.
Then we must find data sources to provide insight into which factors are active and where.

### Factors which create the infection conditions:
* Number of current cases
  * The virus is able to be spread by infected individuals long before they show symptoms
  * This points to the theory that in the short-term, areas with higher numbers of known cases are more likely to have higher numbers of unknown cases
* Population density
  * Regions with greater population density will have higher probabilities of bringing infected hosts into contact with non-infected hosts
* Transportation
  * Areas with high useage of public transportation are probably more likely to spread the virus
    * For instance, people riding a subway are more likely to be in close contact with one another than people who commute via personal cars
  * Areas with higher numbers of incoming flights are more likely to see new cases
    * Flights provide a close proximity environment where people could spread the virus
* PPE shortages
  * Areas where hospitals are running low on PPE supplies (gloves, N95 masks, hand sanitizer) could see higher rates of infection as healthcare workers come into contact with infected individuals without the use of PPE
* Hospital infrastructure
  * Hospitals will more facilities to treat infected patients could provide better opportunities for isolation of the infected
    * Infrastrucutre such as negative pressure rooms and ICU beds will allow for proper containment within the hospital
    * If this infrastructure becomes overwhelmed, patients are more likely to be treated in areas which lack proper containment capability. This could increase infection probability among healthcare staff.
* Lack of government resonse
  * Areas where the local, state, or federal government has taken less action will likely see faster spread of the virus
    * For instance, in Pennsylvania the governor has just suspended the activity of all non-essential businesses
    * States or areas with similar population density who have yet taken similar precautions will likely see higher numbers of infected cases
* Availability of testing
  * Areas which lack the ability to properly screen for the virus will be fighting with a blindfold on
    * It will be difficult to predict accurate infection rates in these zones
    * It is probably a safe assumption to assume these areas will see faster and higher rates of infections as they will be unable to perform proper containment procedures
* Number of recovered cases
  * Areas with higher numbers of recovered individuals will be more likely to have herd immunity to the virus
    * Note: medical professionals say that while it is statistically possible to be infected twice, it is extremely unlikely
    * Therefore herd immunity still stands as a viable limiting factor to the virus, at least in the short term
    * SOURCE: https://www.theguardian.com/world/2020/mar/16/the-big-question-over-coronavirus-can-a-person-get-it-twice


### Factors that increase risk of death from SARS-COV-2:
* Demographics
  * Currently age seems to be the only demographic that effects the severity of the virus
    * Those who are older seem to be more likely to suffer complications or even death from the virus
    * It is important to note, age does NOT seem to affect the ability of the virus to spread
      * So far those in their 20's seems just as likely to contract the virus as those in their 70's
      * SOURCE: https://www.cdc.gov/coronavirus/2019-ncov/specific-groups/high-risk-complications/older-adults.html
* Health complications   
  * Individuals with health complications such as immunodeficiencies due to prior/ongoing illnesses are more likely to be placed in critical care
  * It is most likely impossible to obtain this data due to HIPAA laws
* Number of reported cases
  * Areas with higher reported cases will be more likely to see their healthcare systems overwhelmed
    * Overwhelmed healthcare facilities can cause:
      * A shortage of medical infrastructure such as ICU beds and ventilators, resulting in triage and an increase in deaths
      * A shortage of PPE such as N95 masks and gloves, resulting in more likely infection of hospital staff, which in turn could increase deaths as caretakers could become overworked and spread thin


### Note:
* We should not take climate (humidity, etc.) into account. This does not seem to currently affect the spread of the virus.
* SOURCE: https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public/myth-busters

# TODO:

### Datasources to be cleaned and fed into a model:
* Note: This data must be able to be grouped by geographical region
  * The granularity of the region may vary, but results will most likely be increasingly more accurate with finer granularity of region
  * For instance, if data is able to be collected for each county analyzed, this would be much better than simply obtaining state-wide data

* Note: The data sourced might need to have data spanshots over time. For instance the model might need to be trained with data reported daily for two weeks time.
  * If this is the case we will need data, such as PPE shortages, that has been reported daily.
  * This depends on how we implement the model

### Factors which create the infection conditions:
* Number of current cases
  * https://www.nytimes.com/interactive/2020/us/coronavirus-us-cases.html#g-cases-by-county
    * Search "counties" to find county data
    * This source is updated daily, but might not contain complete data as the New York Times is a news publication, not a government database

* Population density

* Transportation

* PPE shortages

* Hospital infrastructure

* Lack of government resonse

* Availability of testing

* Number of recovered cases
