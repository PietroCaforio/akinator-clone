# akinator-clone

### Requirements
This project uses **Conda** for environment management.

To set up everything:

```bash
make deps      # Create the Conda environment
make data      # Download the dataset
```

#### To start the backend:
```bash
uvicorn backend.main:app --reload
```

### To setup and start the frontend:
```bash
cd akinator-frontend
npm install
npm run dev
```

## TODOs

- Add support for new answer types: "Not sure", "Probably", etc.

- Enable adding new characters with custom questions via the interface.

- Extend the application to run on the full dataset (not just the small demo).

- Improve frontend UI/UX appearance (styling, responsiveness, animations).

- Track answer confidence or ambiguity and visualize it in results.

- Add persistent storage (e.g., database) to save sessions and user inputs.

- Support mobile-friendly layout.

- Implement a "restart game" and "back to previous question" button.