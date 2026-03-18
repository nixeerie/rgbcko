# 🎨 RGB Gradient Creator

A beautiful, modern Flask web application for creating custom color gradients with an elegant glass-morphism design.

## ✨ Features

- **Beautiful UI**: Modern glass-morphism design with smooth animations
- **Interactive Gradient Circle**: Animated pulsing gradient display in the center
- **Color Input Validation**: Smart validation with Czech language support
- **Color Palette**: 200+ named colors in an interactive scrollable grid
- **Selective Color Application**: Choose which color field to update from palette
- **Gradient History**: Save and reload previous gradients
- **Responsive Design**: Works beautifully on desktop, tablet, and mobile
- **Real-time Feedback**: Instant validation and error messages

## 🎯 Usage

- Enter hex color codes in the form (e.g., #FF0000 for red)
- Enter color names from the palette (e.g., "Red", "Blue", "Pink")
- Invalid colors will show error messages and won't be accepted
- Use the color palette below the form to quickly select colors by name
- Choose which color field (1, 2, or 3) to apply the selected color to
- Click "Vymazat" to clear a specific color field
- Click "Vytvoř gradient" to generate the gradient
- View your gradient history in the right panel
- Click "Načíst" to load a previous gradient
- Click "Vymazat historii" to clear all saved gradients

## 🎨 Design Features

- **Glass-morphism panels** with backdrop blur effects
- **Smooth animations** and hover effects
- **Gradient backgrounds** and pulsing circle animation
- **Modern typography** with Poppins font
- **Responsive grid layouts** for all screen sizes
- **Interactive color picker** with name tooltips

## 🔧 Color Validation

The app validates all color inputs:
- **Hex codes**: Must be in format #RRGGBB (e.g., #FF0000)
- **Color names**: Must match names from the color palette (case-insensitive)
- **Auto-conversion**: Color names are automatically converted to hex codes
- **Error display**: Invalid colors show red error messages below the input field