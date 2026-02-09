"""
GMS to Tannico Category Mapping
================================
Maps GMS macro_categories to Tannico wine & spirits categories
based on strategic role equivalence methodology.

Dataset: data (DataFrame with 'macro_category' column)
"""

import pandas as pd
import numpy as np

# ============================================================================
# 1. DEFINE MAPPING DICTIONARY
# ============================================================================

# GMS → Tannico Strategic Mapping
gms_to_tannico_mapping = {
    'apparel': 'Red Wines',
    'lifestyle': 'White & Rosé Wines',
    'collections': 'Sparkling Wines & Champagne',
    'stationery': 'Spirits & Liqueurs',
    'new': 'Gift Boxes',
    'shop by brand': 'Accessories',
    'uncategorized': 'Gourmet Products',
    'sale': 'Outlet'
}

# Category strategic roles for reference
tannico_strategic_roles = {
    'Red Wines': 'Volume Foundation',
    'White & Rosé Wines': 'Volume Co-Driver',
    'Sparkling Wines & Champagne': 'Margin Maximizer',
    'Spirits & Liqueurs': 'Premium Margin',
    'Gift Boxes': 'Seasonal Boost',
    'Accessories': 'Cross-sell',
    'Gourmet Products': 'Basket Builder',
    'Outlet': 'Tactical Cash',
    'Other': 'Innovation Lab'
}

# Category priority (for sorting/analysis)
tannico_priority = {
    'Red Wines': 1,
    'White & Rosé Wines': 2,
    'Sparkling Wines & Champagne': 3,
    'Spirits & Liqueurs': 4,
    'Gift Boxes': 5,
    'Accessories': 6,
    'Gourmet Products': 7,
    'Outlet': 8,
    'Other': 9
}

# ============================================================================
# 2. APPLY MAPPING TO DATAFRAME
# ============================================================================

print("="*70)
print("APPLYING GMS → TANNICO CATEGORY MAPPING")
print("="*70)

# Check if macro_category column exists
if 'macro_category' not in data.columns:
    print("❌ ERROR: 'macro_category' column not found in dataframe")
    print(f"Available columns: {data.columns.tolist()}")
else:
    print("✅ Found 'macro_category' column")
    
    # Create new column with Tannico categories
    data['tannico_category'] = data['macro_category'].map(gms_to_tannico_mapping)
    
    # Add strategic role column
    data['tannico_strategic_role'] = data['tannico_category'].map(tannico_strategic_roles)
    
    # Add priority for sorting
    data['tannico_priority'] = data['tannico_category'].map(tannico_priority)
    
    # Check for unmapped categories
    unmapped = data[data['tannico_category'].isna()]
    
    if len(unmapped) > 0:
        print(f"\n⚠️  WARNING: Found {len(unmapped)} rows with unmapped categories:")
        print(unmapped['macro_category'].value_counts())
        print("\n💡 These will be mapped to 'Other' category")
        
        # Map unmapped to 'Other'
        data['tannico_category'].fillna('Other', inplace=True)
        data['tannico_strategic_role'].fillna('Innovation Lab', inplace=True)
        data['tannico_priority'].fillna(9, inplace=True)
    else:
        print("\n✅ All categories successfully mapped!")
    
    print(f"\n📊 Total rows processed: {len(data):,}")

# ============================================================================
# 3. VALIDATION & SUMMARY STATISTICS
# ============================================================================

print("\n" + "="*70)
print("MAPPING VALIDATION & SUMMARY")
print("="*70)

# Convert revenue to numeric if it exists (CRITICAL FIX)
if 'transaction_revenue_usd' in data.columns:
    print("\n🔧 Converting revenue column to numeric...")
    data['transaction_revenue_usd'] = pd.to_numeric(data['transaction_revenue_usd'], errors='coerce')
    data['transaction_revenue_usd'].fillna(0, inplace=True)
    print(f"✅ Revenue column converted: {data['transaction_revenue_usd'].dtype}")

# Count by Tannico category
print("\n📊 Distribution by Tannico Category:")
tannico_dist = data['tannico_category'].value_counts().sort_values(ascending=False)
print(tannico_dist)

# Calculate revenue by Tannico category (if revenue column exists)
if 'transaction_revenue_usd' in data.columns:
    print("\n💰 Revenue by Tannico Category:")
    
    revenue_by_tannico = data.groupby('tannico_category')['transaction_revenue_usd'].agg([
        ('Total_Revenue', 'sum'),
        ('Avg_Transaction', 'mean'),
        ('Count', 'count')
    ]).sort_values('Total_Revenue', ascending=False)
    
    # Add percentage
    revenue_by_tannico['% of Revenue'] = (
        revenue_by_tannico['Total_Revenue'] / revenue_by_tannico['Total_Revenue'].sum() * 100
    ).round(2)
    
    print(revenue_by_tannico)
    
    # Validate against wine industry benchmarks
    print("\n" + "="*70)
    print("BENCHMARK VALIDATION vs Wine Industry Standards")
    print("="*70)
    
    # Volume Drivers (should be 60-70%)
    volume_drivers = revenue_by_tannico.loc[
        revenue_by_tannico.index.isin(['Red Wines', 'White & Rosé Wines'])
    ]['% of Revenue'].sum()
    
    # Margin Drivers (should be 15-25%)
    margin_drivers = revenue_by_tannico.loc[
        revenue_by_tannico.index.isin(['Sparkling Wines & Champagne', 'Spirits & Liqueurs'])
    ]['% of Revenue'].sum()
    
    # Ancillary (should be 10-15%)
    ancillary = revenue_by_tannico.loc[
        revenue_by_tannico.index.isin(['Accessories', 'Gift Boxes', 'Gourmet Products'])
    ]['% of Revenue'].sum()
    
    # Tactical (should be 5-10%)
    tactical = revenue_by_tannico.loc[
        revenue_by_tannico.index.isin(['Outlet', 'Other'])
    ]['% of Revenue'].sum()
    
    print(f"\n🎯 Volume Drivers (Target: 60-70%): {volume_drivers:.1f}%", 
          "✅" if 55 <= volume_drivers <= 75 else "⚠️")
    print(f"💎 Margin Drivers (Target: 15-25%): {margin_drivers:.1f}%",
          "✅" if 12 <= margin_drivers <= 28 else "⚠️")
    print(f"🎁 Ancillary (Target: 10-15%): {ancillary:.1f}%",
          "✅" if 8 <= ancillary <= 20 else "⚠️")
    print(f"🔄 Tactical (Target: 5-10%): {tactical:.1f}%",
          "✅" if 3 <= tactical <= 12 else "⚠️")
    
    # Overall validation
    total_check = volume_drivers + margin_drivers + ancillary + tactical
    print(f"\n📊 Total: {total_check:.1f}%", "✅" if 99 <= total_check <= 101 else "⚠️")

# ============================================================================
# 4. CREATE SUMMARY DATAFRAME
# ============================================================================

print("\n" + "="*70)
print("CREATING SUMMARY DATAFRAME")
print("="*70)

# Create comprehensive summary
tannico_summary = data.groupby(['tannico_category', 'tannico_strategic_role']).agg({
    'transaction_revenue_usd': ['sum', 'mean', 'count']
}).round(2)

# Flatten column names
tannico_summary.columns = ['Total_Revenue_USD', 'Avg_Transaction_USD', 'Transaction_Count']
tannico_summary = tannico_summary.reset_index()

# Add percentage and priority
tannico_summary['Revenue_Percentage'] = (
    tannico_summary['Total_Revenue_USD'] / tannico_summary['Total_Revenue_USD'].sum() * 100
).round(2)

tannico_summary['Priority'] = tannico_summary['tannico_category'].map(tannico_priority)

# Sort by priority
tannico_summary = tannico_summary.sort_values('Priority')

print("\n📊 Tannico Category Summary:")
print(tannico_summary.to_string(index=False))

# ============================================================================
# 5. ORIGINAL GMS TO TANNICO MAPPING REFERENCE
# ============================================================================

print("\n" + "="*70)
print("GMS → TANNICO MAPPING REFERENCE")
print("="*70)

# Create mapping reference table
mapping_reference = []

for gms_cat, tannico_cat in gms_to_tannico_mapping.items():
    # Get stats for this GMS category
    gms_stats = data[data['macro_category'] == gms_cat].agg({
        'transaction_revenue_usd': ['sum', 'mean', 'count']
    })
    
    mapping_reference.append({
        'GMS_Category': gms_cat,
        'Tannico_Category': tannico_cat,
        'Strategic_Role': tannico_strategic_roles[tannico_cat],
        'Transaction_Count': int(gms_stats['transaction_revenue_usd']['count']),
        'Total_Revenue': float(gms_stats['transaction_revenue_usd']['sum']),
        'Avg_Transaction': float(gms_stats['transaction_revenue_usd']['mean'])
    })

mapping_df = pd.DataFrame(mapping_reference)
mapping_df['Revenue_Pct'] = (mapping_df['Total_Revenue'] / mapping_df['Total_Revenue'].sum() * 100).round(2)

print("\n" + mapping_df.to_string(index=False))

# ============================================================================
# 6. EXPORT RESULTS (OPTIONAL)
# ============================================================================

print("\n" + "="*70)
print("DATA EXPORT OPTIONS")
print("="*70)

# Save mapped dataframe
# data.to_csv('data_with_tannico_mapping.csv', index=False)
# print("✅ Full dataset exported to: data_with_tannico_mapping.csv")

# Save summary
# tannico_summary.to_csv('tannico_category_summary.csv', index=False)
# print("✅ Summary exported to: tannico_category_summary.csv")

# Save mapping reference
# mapping_df.to_csv('gms_tannico_mapping_reference.csv', index=False)
# print("✅ Mapping reference exported to: gms_tannico_mapping_reference.csv")

print("\n💡 Uncomment export lines above to save results to CSV")

# ============================================================================
# 7. SAMPLE DATA PREVIEW
# ============================================================================

print("\n" + "="*70)
print("SAMPLE DATA PREVIEW (First 10 rows)")
print("="*70)

# Show sample with new columns
sample_cols = ['event_date', 'event_name', 'macro_category', 'tannico_category', 
               'tannico_strategic_role', 'transaction_revenue_usd']
available_cols = [col for col in sample_cols if col in data.columns]

print("\n" + data[available_cols].head(10).to_string(index=False))

# ============================================================================
# 8. QUICK ACCESS VARIABLES
# ============================================================================

print("\n" + "="*70)
print("QUICK ACCESS VARIABLES CREATED")
print("="*70)

print("""
✅ New columns added to 'data' DataFrame:
   - tannico_category: Mapped Tannico category
   - tannico_strategic_role: Strategic role (Volume/Margin/Support/Tactical)
   - tannico_priority: Numeric priority (1-9) for sorting

✅ Summary DataFrames created:
   - tannico_summary: Aggregated stats by Tannico category
   - mapping_df: GMS to Tannico mapping reference with stats

✅ Dictionaries available:
   - gms_to_tannico_mapping: Direct mapping dict
   - tannico_strategic_roles: Category to role mapping
   - tannico_priority: Category to priority mapping

📊 Example usage:
   # Filter by Tannico category
   red_wines_data = data[data['tannico_category'] == 'Red Wines']
   
   # Analyze by strategic role
   volume_drivers = data[data['tannico_strategic_role'].str.contains('Volume')]
   
   # Sort by priority
   data_sorted = data.sort_values('tannico_priority')
""")

print("\n" + "="*70)
print("✅ MAPPING COMPLETE!")
print("="*70)
print(f"\n📊 Total rows: {len(data):,}")
print(f"🍷 Tannico categories: {data['tannico_category'].nunique()}")
print(f"📈 Ready for Tannico-lens analysis!")
print("\n" + "="*70)