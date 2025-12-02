"use client";

import { useState, useRef, useEffect } from "react";

// Type for filter options
type FilterStatus = "All" | "Active" | "Paused";

interface FilterDropdownProps {
  currentFilter: FilterStatus;
  onFilterChange: (filter: FilterStatus) => void;
}

/**
 * FilterDropdown Component
 * 
 * A reusable dropdown component for filtering campaigns by status.
 * Supports clicking outside to close the dropdown.
 */
export default function FilterDropdown({
  currentFilter,
  onFilterChange,
}: FilterDropdownProps) {
  const [isOpen, setIsOpen] = useState<boolean>(false);
  const dropdownRef = useRef<HTMLDivElement>(null);

  // Filter options
  const filterOptions: FilterStatus[] = ["All", "Active", "Paused"];

  // Close dropdown when clicking outside
  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (
        dropdownRef.current &&
        !dropdownRef.current.contains(event.target as Node)
      ) {
        setIsOpen(false);
      }
    };

    document.addEventListener("mousedown", handleClickOutside);
    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, []);

  // Handle filter selection
  const handleSelect = (filter: FilterStatus) => {
    onFilterChange(filter);
    setIsOpen(false);
  };

  return (
    <div className="relative" ref={dropdownRef}>
      {/* Dropdown Button */}
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="flex items-center gap-2 px-4 py-2 bg-white border border-gray-300 rounded-lg shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition-colors"
        aria-haspopup="true"
        aria-expanded={isOpen}
      >
        <span className="text-sm font-medium text-gray-700">
          Filter: {currentFilter}
        </span>
        <svg
          className={`w-4 h-4 text-gray-500 transition-transform ${
            isOpen ? "rotate-180" : ""
          }`}
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M19 9l-7 7-7-7"
          />
        </svg>
      </button>

      {/* Dropdown Menu */}
      {isOpen && (
        <div className="absolute right-0 mt-2 w-48 bg-white border border-gray-200 rounded-lg shadow-lg z-10">
          <div className="py-1">
            {filterOptions.map((option) => (
              <button
                key={option}
                onClick={() => handleSelect(option)}
                className={`w-full text-left px-4 py-2 text-sm transition-colors ${
                  currentFilter === option
                    ? "bg-blue-50 text-blue-700 font-medium"
                    : "text-gray-700 hover:bg-gray-50"
                }`}
              >
                {option}
              </button>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

