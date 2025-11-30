# Exploring NASA GPM IMERG Precipitation Data (Half-Hourly, V07 Final Run)
## 1. Dataset Identification

I started my search by browsing different Earth system datasets listed in the homework instructions. NASA **GPM IMERG precipitation dataset** immediately caught my interest, because I work with ground-based rain-rate measurements (e.g., Parsivel disdrometers). I wanted to understand how global precipitation products compare. IMERG will help me explore precipitation from a global, satellite-based perspective rather than point-wise ground sensors.

I selected **IMERG Half-Hourly Final Run (V07)** because:

- Global precipitation coverage  
- 0.1° × 0.1° spatial resolution  
- 30-minute temporal resolution  
- Freely available  
- Well documented  
- Perfect for data-access workflow evaluation  

---

## Searching & Navigating Data Portals

I started at NASA’s IMERG information page and navigated into the GES DISC data archive. The dataset structure was straightforward:
- Dataset: GPM_3IMERGHH.07 (Half-hourly, Version 07)
- Runs: Early(GPM_3IMERGHHE), Late(GPM_3IMERGHHL), Final(GPM_3IMERGHH). I chose Final

Directory layout:
/YEAR/DAY-OF-YEAR (001–365)/48 × half-hourly HDF5 files


Example directory I worked with:

https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGHH.07/2025/122/


Before downloading, I registered for an Earthdata Login. You can register here:
https://urs.earthdata.nasa.gov/home

Then I went to the Applications Tab, and clicked on "Approve more Applications". From the list I selected the **NASA GESDISC DATA ARCHIVE** and approved it. This allows you to now download the dataset in question.

The interface was well organized:
- Navigating by year → day-of-year felt intuitive
- Files were clearly named
- Metadata files (.xml) are provided as well

Download options include GUI (browser) or automated Python access

---


## 3. Dataset Documentation

NASA provides excellent documentation. The following URLs were essential:

###  IMERG Product Overview  
https://gpm.nasa.gov/data/imerg

### FAQ for IMERG V07 Applications Users_202502.pdf 
https://gpm.nasa.gov/media/708

### GES DISC IMERG Product Page  
https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGHH_07/summary

These explained:

- Data sources (microwave + IR sensors)  
- Multi-satellite merging  
- Differences between Early/Late/Final   
- File naming conventions  
- Directory structure  

Everything was well linked and beginner-friendly.

---

## 4. Authentication & Technical Workflow

GES DISC requires **Earthdata login authentication**, no API token needed.

###  Creating `.netrc`

```bash
vi ~/.netrc
```
Contents:
```bash
machine urs.earthdata.nasa.gov
    login <my-email>
    password <my-password>
```
NASA requires strict permissions, so I set:
```bash
chmod 600 ~/.netrc
```

Python authenticated download:

```python
session = requests.Session()
session.trust_env = True
```
Working with HDF5
```python
import h5py

f = h5py.File("example.h5", "r")
list(f["Grid"].keys())
```

This gave access to:

- precipitation
- randomError
- probabilityLiquidPrecipitation
- precipitationQualityIndex
- lat, lon
- time, time_bnds
  
Opening HDF5 files with the h5py library was straightforward — I could inspect the dataset tree, shapes, metadata, and attributes easily.
The only limitation is that IMERG files must be downloaded entirely; variable-level subsetting isn’t supported.

---

## 5. Understanding the File Structure

The naming convention was intuitive after brief inspection:

Example:
```
3B-HHR.MS.MRG.3IMERG.20250502-S000000-E002959.0000.V07B.HDF5
```

Meaning:
- 20250502-Date
- S000000–E002959-00:00–00:29 UTC
- 48 such files per day
- V07B-Version
- HHR-Half-hourly Final Run ("HH"=Half-hourly, “R” = Final)
- Daily directory structure uses Day-of-Year (DOY), e.g.: 122=2 May 2025

Once I understood this, navigation was trivial.

---

## 6. Evaluation of the Data Portal (GES DISC)

Overall, the GES DISC portal was extremely smooth to use:

- Clean folder structure
- Clear documentation
- Simple Earthdata authentication
- No API complexities (just .netrc)
- Direct HTML directory listings
- Fast downloads
- Beginner friendly
- GUI and Python both supported

Only drawback:
You must download full HDF5 files rather than selecting individual variables.
Otherwise, it is an excellent, accessible, well-organized platform for scientific data.

---

## 7. AI Assistance Documentation

I used ChatGPT for the following verified queries:

- Setting up a `.netrc` file for NASA Earthdata authentication:
  - Helped me switch from `nano` (not installed) to `vi`
  - Helped ensure correct indentation and permissions

- Opening an HDF5 file with `h5py`:
  - I had never parsed HDF5 before
  - ChatGPT helped me explore the tree structure and attributes

- Finding a “glob”-like way to list files:
  - ChatGPT recommended using BeautifulSoup to parse HTML directory listings
  - This approach worked very well
  - All information was verified manually by testing and consulting NASA documentation.
