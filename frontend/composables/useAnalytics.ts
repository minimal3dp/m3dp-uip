export const useAnalytics = () => {
  const trackCalculatorUse = (calculator: string, data?: Record<string, any>) => {
    try {
      if (typeof window !== 'undefined' && (window as any).gtag) {
        (window as any).gtag('event', 'calculator_use', {
          calculator,
          ...data,
        });
      }
    } catch (_) {
      // swallow analytics errors silently
    }
  };

  return { trackCalculatorUse };
};
