# MLB Props Predictor - Frontend

A React application built with Vite and Tailwind CSS for predicting MLB player props.

## Technology Stack

- **React** - Frontend framework
- **Vite** - Build tool and development server
- **Tailwind CSS** - Utility-first CSS framework

## Prerequisites

- Node.js (v16 or higher)
- npm or yarn package manager

## Installation

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

## Running the Application

### Development Mode

Start the development server:
```bash
npm run dev
```

The application will be available at `http://localhost:5173`

### Build for Production

Create a production build:
```bash
npm run build
```

### Preview Production Build

Preview the production build locally:
```bash
npm run preview
```

## Project Structure

```
frontend/
├── public/          # Static assets
├── src/             # Source code
│   ├── components/  # React components
│   ├── assets/      # Images, icons, etc.
│   ├── App.jsx      # Main app component
│   ├── index.css    # Global styles with Tailwind
│   └── main.jsx     # Entry point
├── index.html       # HTML template
├── package.json     # Dependencies and scripts
├── tailwind.config.js # Tailwind CSS configuration
└── vite.config.js   # Vite configuration
```

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint

## Notes

- The development server runs on port 5173 by default
- The backend API is expected to run on `http://localhost:8000`
- Tailwind CSS is configured and ready to use
