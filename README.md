# Inventory_management_system

A step-by-step instructions to get started with an Inventory Management System Django project that includes a requirements.txt file. This assumes you have Python and Django already installed on your system:
### Getting Started

Inventory Management System is which provides powerful low-level stock control and part tracking. The core of the IMS system is a Python/Django database backend which provides an admin interface (web-based). A powerful plugin system provides support for custom applications and extensions for viewing editing and managing the products costumers and a over all order and currency flow in the system. TO get started :


1. **Clone the Repository**:

   You can follow this general guide on cloning a Git repository: [Cloning a Repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo)

2. **Create a Virtual Environment** (optional but recommended):

   You can find detailed instructions for creating and activating a virtual environment in Python here: [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

3. **Install Dependencies**:

   Installing Python packages from a `requirements.txt` file can be done with the following command:

   ```
   pip install -r requirements.txt
   ```

4. **Database Setup**:
   - Create the database tables by running migrations:
     ```
     python manage.py migrate
     ```
   - (Optional) Load initial data (e.g., sample categories, products):
     ```
     python manage.py loaddata initial_data.json
     ```
5. **Create a Superuser**:
   Create an admin user to access the Django admin interface:
   ```
   python manage.py createsuperuser
   ```
   Follow the prompts to set up the admin username and password.

6. **Run the Development Server**:
   Start the development server:
   ```
   python manage.py runserver
   ```
   This will run your application locally. You can access it in your web browser at `http://localhost:8000/`.

7. **Access the Admin Panel**:
   To access the admin panel, go to `http://localhost:8000/admin/` and log in with the superuser credentials created earlier. Here, you can manage categories, products, and other data related to the inventory.

8. **Start Using the Application**:

   You can now start using the Inventory Management System. Depending on the features and functionality of your specific project, users can interact with the system to manage inventory, add products, view reports, etc.

## for admin the homepage may look as( click to view ):

[![Admin_view](https://img.youtube.com/vi/3YNe3_y4OGs/0.jpg)](https://www.youtube.com/watch?v=3YNe3_y4OGs)

## for costumer or user the homepage may look as( click to view ):

[![Costumer_view](https://img.youtube.com/vi/YilbyB_mVJU/0.jpg)](https://www.youtube.com/watch?v=YilbyB_mVJU)

## Deployment done in heruko 

   You can find detailed instructions for deploying the serverbased code as django in Heruko here: [Heruko deployment Environments](https://devcenter.heroku.com/articles/how-heroku-works)
