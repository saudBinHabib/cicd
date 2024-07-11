# Git Practice Exercise

In this exercise, you will practice using various Git commands to manage a repository. Follow the instructions below to complete the exercise.

## Step 1: Clone the Repository

1. Open your terminal.
2. Navigate to the directory where you want to clone the repository.
3. Run the following command to clone the repository:

   ```
   git clone <repository-url>
   ```

   Replace `<repository-url>` with the URL of the repository you want to clone.

## Step 2: Create a New Branch

1. Change to the repository's directory:

   ```
   cd <repository-directory>
   ```

   Replace `<repository-directory>` with the name of the cloned repository's directory.

2. Create a new branch using the following command:

   ```
   git branch <branch-name>
   ```

   Replace `<branch-name>` with a descriptive name for your branch.

3. Switch to the new branch:

   ```
   git checkout <branch-name>
   ```

## Step 3: Make Changes and Commit

1. Open the necessary files in your preferred text editor.
2. Make the desired changes to the files.
3. Save the changes.
4. Stage the changes using the following command:

   ```
   git add .
   ```

5. Commit the changes with a descriptive message:

   ```
   git commit -m "Your commit message"
   ```

## Step 4: Push Changes to Remote Repository

1. Push your changes to the remote repository using the following command:

   ```
   git push origin <branch-name>
   ```

   Replace `<branch-name>` with the name of your branch.

## Step 5: Create a Pull Request

1. Go to the repository's page on GitHub.
2. Click on the "Pull requests" tab.
3. Click on the "New pull request" button.
4. Select your branch as the "base" branch and the main branch as the "compare" branch.
5. Add a descriptive title and comment for your pull request.
6. Click on the "Create pull request" button to submit your pull request.

Congratulations! You have completed the Git practice exercise. Keep practicing and exploring different Git commands to become more proficient with version control.
