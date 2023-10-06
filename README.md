# flask_4_databases_mysql_vm
## **HHA 504 Homework Assignment 4**

## **The VM and MySQL Setup Process**
### Step 1: Create a Virtual Machine on Azure

1. **Log in to the Azure Portal**: Go to the [Azure Portal](https://portal.azure.com/) and sign in to your Azure account.

2. **Create a Virtual Machine**:
   - Click on "Create a resource."
   - Search for "Virtual Machine" and click on it.
   - Follow the wizard to configure your VM, including selecting the operating system, size, and networking settings.
   - Make sure to open the necessary ports (typically 22 for SSH and 3306 for MySQL) in the network security group during VM creation.

### Step 2: Connect to Your Azure VM

1. **SSH into the VM**: Use an SSH client to connect to your Azure VM using the public IP address provided during VM creation.

### Step 3: Install MySQL on Azure VM

1. **Update the Package Repository**:
   ```
   sudo apt-get update
   ```

2. **Install MySQL Server**:
   ```
   sudo apt-get install mysql-server
   ```

3. **Configure MySQL**:
   Follow the prompts to set up a password for the MySQL root user and other configuration options.

4. **Start MySQL**:
   ```
   sudo systemctl start mysql
   ```

5. **Enable MySQL to Start on Boot**:
   ```
   sudo systemctl enable mysql
   ```

### Step 1: Create a Virtual Machine on GCP

1. **Log in to GCP Console**: Go to the [GCP Console](https://console.cloud.google.com/) and sign in to your GCP account.

2. **Create a Virtual Machine**:
   - Click on the navigation menu and go to "Compute Engine" > "VM instances."
   - Click the "Create" button to create a new VM.
   - Configure your VM, including selecting the operating system, machine type, and networking settings.

### Step 2: Connect to Your GCP VM

1. **SSH into the VM**: Click the SSH button next to your VM instance in the GCP Console to open a browser-based SSH terminal or use an SSH client.

### Step 3: Install MySQL on GCP VM

1. **Update the Package Repository**:
   ```
   sudo apt-get update
   ```

2. **Install MySQL Server**:
   ```
   sudo apt-get install mysql-server
   ```

3. **Configure MySQL**:
   Follow the prompts to set up a password for the MySQL root user and other configuration options.

4. **Start MySQL**:
   ```
   sudo systemctl start mysql
   ```

5. **Enable MySQL to Start on Boot**:
   ```
   sudo systemctl enable mysql
   ```

## **Rationale Behind the Database Schema**
This will create a clinical database with three tables: patients, medications, and patient_medications. Additionally, there is a foreign key relationship between the patient_medications table and both the patients and medications tables, which is used to link patients with the medications they are prescribed.

The Schema I Chose and Why:

Database Schema:

1.  patients Table:
    patient_id (Primary Key, automatic): A unique identifier for each patient.
    first_name and last_name: Store the patient's first and last names.
    date_of_birth: Records the patient's date of birth.

2.  medications Table:
    medication_id (Primary Key, automatic): A unique identifier for each medication.
    medication_name: Stores the name of the medication.

3.  patient_medications Table:
    patient_medication_id (Primary Key, automatic): A unique identifier for each patient-medication relationship.
    patient_id (Foreign Key, references patients(patient_id)): Links the patient to their prescribed medications.
    medication_id (Foreign Key, references medications(medication_id)): Links the medication to the patients.
    prescribed_date: Records the date when the medication was prescribed to the patient.

My schema allows me to associate patients with the medications they are prescribed. The patient_id and medication_id fields in the patient_medications table create a foreign key relationship with the patients and medications tables, respectively, establishing the connection between patients and their prescribed medications.

## **Steps and Challenges from the Database Migration Process**

## **Documented Code Errors and Troubleshooting Attempts**