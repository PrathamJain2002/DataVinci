"use client";

import { useState, useEffect } from "react";
import CampaignTable from "@/components/CampaignTable";
import FilterDropdown from "@/components/FilterDropdown";

// Type definition for Campaign
export interface Campaign {
  id: number;
  name: string;
  status: "Active" | "Paused";
  clicks: number;
  cost: number;
  impressions: number;
}

// Type for filter options
type FilterStatus = "All" | "Active" | "Paused";

export default function CampaignsPage() {
  const [campaigns, setCampaigns] = useState<Campaign[]>([]);
  const [filteredCampaigns, setFilteredCampaigns] = useState<Campaign[]>([]);
  const [filter, setFilter] = useState<FilterStatus>("All");
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  // Fetch campaigns from backend
  useEffect(() => {
    const fetchCampaigns = async () => {
      try {
        setLoading(true);
        setError(null);
        
        // Get API URL from environment variable, fallback to localhost
        const apiUrl = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";
        const response = await fetch(`${apiUrl}/campaigns`);

        if (!response.ok) {
          throw new Error(`Failed to fetch campaigns: ${response.statusText}`);
        }

        const data = await response.json();
        setCampaigns(data);
        setFilteredCampaigns(data);
      } catch (err) {
        setError(err instanceof Error ? err.message : "An unknown error occurred");
        console.error("Error fetching campaigns:", err);
      } finally {
        setLoading(false);
      }
    };

    fetchCampaigns();
  }, []);

  // Filter campaigns based on selected filter
  useEffect(() => {
    if (filter === "All") {
      setFilteredCampaigns(campaigns);
    } else {
      setFilteredCampaigns(
        campaigns.filter((campaign) => campaign.status === filter)
      );
    }
  }, [filter, campaigns]);

  // Handle filter change
  const handleFilterChange = (newFilter: FilterStatus) => {
    setFilter(newFilter);
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="mb-6 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
        <h1 className="text-3xl font-bold">Campaign Analytics</h1>
        <FilterDropdown
          currentFilter={filter}
          onFilterChange={handleFilterChange}
        />
      </div>

      {loading && (
        <div className="flex justify-center items-center py-12">
          <div className="text-lg text-gray-600">Loading campaigns...</div>
        </div>
      )}

      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          <p className="font-bold">Error:</p>
          <p>{error}</p>
        </div>
      )}

      {!loading && !error && (
        <CampaignTable campaigns={filteredCampaigns} />
      )}

      {!loading && !error && filteredCampaigns.length === 0 && (
        <div className="text-center py-12 text-gray-600">
          No campaigns found for the selected filter.
        </div>
      )}
    </div>
  );
}

