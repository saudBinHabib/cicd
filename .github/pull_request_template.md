name: Pull Request Template

description: |
Before submitting your pull request, please ensure that you have completed the following checklist:

- [ ] Describe the changes made in this pull request.
- [ ] Ensure that the code follows the project's coding standards and conventions.
- [ ] Write tests for any new functionality or changes made.
- [ ] Update documentation as needed.
- [ ] Assign reviewers to review the changes.
- [ ] Verify that all CI/CD checks pass successfully.

labels:

- pull request

body:

- type: markdown
  attributes:
  value: | ## Description
  Please provide a brief description of the changes made in this pull request.

- type: markdown
  attributes:
  value: | ## Checklist
  Please check off the following items before submitting your pull request:
      - [ ] I have described the changes made in this pull request.
      - [ ] The code follows the project's coding standards and conventions.
      - [ ] I have written tests for any new functionality or changes made.
      - [ ] I have updated documentation as needed.
      - [ ] I have assigned reviewers to review the changes.
      - [ ] All CI/CD checks pass successfully.
